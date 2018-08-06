#!/usr/bin/env python3

import sys
import glob
from bs4 import BeautifulSoup


def mysql_quote(x):
    """Quote the string x using MySQL quoting rules. If x is the empty string,
    return "NULL". Probably not safe against maliciously formed strings, but
    our input is fixed and from a basically trustable source."""
    if not x:
        return "NULL"
    x = x.replace("\\", "\\\\")
    x = x.replace("'", "''")
    x = x.replace("\n", "\\n")
    return "'{}'".format(x)


def page_number(filepath):
    filename = filepath.split("/")[-1]
    number_part = filename[len("page-"):-len(".html")]
    return int(number_part)


def main():
    last_page = max(map(page_number, glob.glob(sys.argv[1] + "/*")))
    # We could also loop using the output of glob, but we use a range for two
    # reasons: (1) if some page number is missing (e.g. if selenium failed to
    # save) this will catch it; (2) the ordering from glob is not in numerical
    # order.
    for page in range(1, last_page + 1):
        with open(sys.argv[1] + f"/page-{page}.html", "r") as f:
            soup = BeautifulSoup(f, "lxml")
            print_sql(soup_to_grants(soup))


def soup_to_grants(soup):
    for result in soup.find_all("section", {"class": "grantResult"}):
        grantee = result.find("h1").text.strip()
        url = result.find("h1").find("a")["href"]

        tag = result.find("header")
        while tag.name != "p":
            tag = tag.next_sibling
        purpose = tag.text.strip()

        date_amount = result.find("span", {"class": "date"}).text.strip()
        # We will split the date from the amount using the single occurrence of "$"
        assert date_amount.count("$") == 1
        dollar_loc = date_amount.index("$")
        donation_date = date_amount[:dollar_loc].strip()
        amount = date_amount[dollar_loc:].strip()

        location = result.find("div", {"class": "geo-focus"}).text.strip()
        yield {
                "grantee": grantee,
                "url": url,
                "purpose": purpose,
                "donation_date": donation_date,
                "amount": amount,
                "location": location,
                }


def print_sql(grants_generator):
    insert_stmt = """insert into donations (donor, donee, amount, donation_date, donation_date_precision, donation_date_basis, cause_area, url, donor_cause_area_url, notes, affected_cities) values"""
    first = True
    for grant in grants_generator:
        if first:
            print(insert_stmt)
        print(("    " if first else "    ,") + "(" + ",".join([
            mysql_quote("W. K. Kellogg Foundation"),  # donor
            mysql_quote(grant["grantee"]),  # donee
            str(grant["amount"]),  # amount
            mysql_quote(grant["donation_date"]),  # donation_date
            mysql_quote("day"),  # donation_date_precision
            mysql_quote("donation log"),  # donation_date_basis
            mysql_quote(""),  # cause_area
            mysql_quote(grant["url"]),  # url
            mysql_quote(""),  # donor_cause_area_url
            mysql_quote("Purpose: " + grant["purpose"]),  # notes
            mysql_quote(grant["location"]),  # affected_cities
        ]) + ")")
        first = False
    if not first:
        # If first is still true, that means we printed nothing above,
        # so no need to print the semicolon
        print(";")


if __name__ == "__main__":
    main()

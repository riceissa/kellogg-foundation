#!/usr/bin/env python3

import sys
import glob
from bs4 import BeautifulSoup

import pdb


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
            for grant in soup_to_grants(soup):
                print(grant)


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


if __name__ == "__main__":
    main()

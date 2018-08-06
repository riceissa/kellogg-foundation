#!/usr/bin/env python3

import sys
import glob
import datetime
from bs4 import BeautifulSoup


US_STATES = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
             'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
             'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
             'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
             'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
             'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
             'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
             'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
             'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin',
             'Wyoming']

COUNTRIES = ['USA', 'U.S.', 'Mexico', 'Haiti', 'Honduras', 'Virgin Islands', 'Grenada',
             'Puerto Rico', 'Brazil', 'Argentina', 'Zimbabwe', 'Guatemala',
             'Mozambique', 'Lesotho', 'South Africa', 'Botswana', 'Bolivia',
             'Peru', 'Swaziland', 'Chile', 'Colombia', 'Nicaragua', 'Ecuador',
             'Uruguay', 'Malawi', 'Panama', 'El Salvador', 'Costa Rica',
             'Belize', 'Canada', 'Venezuela', 'Jamaica', 'Paraguay',
             'Saint Vincent and the Grenadines', 'Saint Kitts and Nevis',
             'Saint Lucia', 'Cameroon', 'Kenya', 'Antigua and Barbuda',
             'New Zealand', 'United Kingdom', 'Trinidad and Tobago',
             'Dominica', 'Barbados', 'Montserrat']

MEXICO_STATES = ["Aguascalientes", "Baja California", "Baja California Sur",
                 "Campeche", "Chiapas", "Mexico City", "Chihuahua", "Coahuila de Zaragoza",
                 "Colima", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco",
                 "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca",
                 "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa",
                 "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz de Ignacio de la Llave",
                 "Ignacio de la Llave", "Yucatán", "Zacatecas", "Distrito Federal"]

BRAZIL_STATES = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
                 "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
                 "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
                 "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
                 "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
                 "Roraima", "Santa Catarina", "São Paulo", "Sergipe",
                 "Tocantins"]

PERU_REGIONS = ["La Libertad", "Puno"]
CHILE_REGIONS = ["Región Metropolitana de Santiago"]
INDIA_STATES = ["Andhra Pradesh"]
SWAZILAND_REGIONS = ["Hhohho", "Lubombo", "Manzini", "Shiselweni"]
MOZAMBIQUE_PROVINCES = ["Manica", "Sofala"]

SOUTH_AFRICA_PROVINCES = ["Gauteng", "Western Cape", "Kwazulu-Natal", "Free State",
                          "Mpumalanga"]

FRANCE_DEPARTMENTS = ["Val-de-Marne"]

COSTA_RICA_PROVINCES = ["Limón"]
CHINA_PROVINCES = ["Sichuan"]
NEW_ZEALAND_REGIONS = ["Canterbury"]
UNITED_KINGDOM_COUNTIES = ["Buckinghamshire"]

ZIMBABWE_PROVINCES = ["Manicaland", "Harare"]

EL_SALVADOR_DEPARTMENTS = ["Ahuachapán", "Cabañas", "Chalatenango", "Cuscatlán",
                           "La Libertad", "La Paz", "La Unión", "Morazán",
                           "San Miguel", "San Salvador", "San Vicente",
                           "Santa Ana", "Sonsonate", "Usulután"]

HONDURAS_DEPARTMENTS = ["Atlántida"]

CITIES = {
        "Cuneo": "Italy",
        "Bergamo": "Italy",
        "São Paulo": "Brazil",
        "Paris": "France",
        "Zürich (de)": "Switzerland",
        "Maseru": "Lesotho",
        }

HAITI_DEPARTMENTS = ["Artibonite", "Centre", "Grand'Anse", "Nippes", "Nord",
                     "Nord Est", "Nord Ouest", "Ouest", "Sud Est", "Sud"]

def get_location(locations):
    for location in locations:
        if location in US_STATES:
            pass
        elif location.endswith(" Wide") and location[:-len(" Wide")] in COUNTRIES:
            pass
        elif location in COUNTRIES:
            pass
        elif location in MEXICO_STATES:
            pass
        elif location in HAITI_DEPARTMENTS:
            pass
        elif location in FRANCE_DEPARTMENTS:
            pass
        elif location in SOUTH_AFRICA_PROVINCES:
            pass
        elif location in PERU_REGIONS:
            pass
        elif location in EL_SALVADOR_DEPARTMENTS:
            pass
        elif location in BRAZIL_STATES:
            pass
        elif location in COSTA_RICA_PROVINCES:
            pass
        elif location in ZIMBABWE_PROVINCES:
            pass
        elif location in HONDURAS_DEPARTMENTS:
            pass
        elif location in CHILE_REGIONS:
            pass
        elif location in INDIA_STATES:
            pass
        elif location in CHINA_PROVINCES:
            pass
        elif location in MOZAMBIQUE_PROVINCES:
            pass
        elif location in NEW_ZEALAND_REGIONS:
            pass
        elif location in UNITED_KINGDOM_COUNTIES:
            pass
        elif location in SWAZILAND_REGIONS:
            pass
        elif location in CITIES:
            pass
        elif location == "American Indian/Alaska Tribal Nation":
            pass
        elif location == "DR Wide":
            # Dominican Republic, e.g. https://www.wkkf.org/grants/grant/2009/01/improving-and-consolidating-a-rural-development-experience-3010662
            pass
        else:
            print(location, file=sys.stderr)
    return "blah"

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
        # print(f"Doing page {page}", file=sys.stderr)
        with open(sys.argv[1] + f"/page-{page}.html", "r") as f:
            soup = BeautifulSoup(f, "lxml")
            print_sql(soup_to_grants(soup, page, last_page))


def soup_to_grants(soup, page, last_page):
    grant_result = soup.find_all("section", {"class": "grantResult"})
    # Make sure we have a full page of grants
    assert page == last_page or len(grant_result) == 100
    for result in grant_result:
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
        date_range = date_amount[:dollar_loc].strip()
        donation_date = ""
        donation_date_precision = ""
        grant_range = ""
        if date_range:
            start_date, end_date = date_range.split(" - ")
            # For some reason, the months appear both in the full form and in
            # abbreviated form
            try:
                donation_date = datetime.datetime.strptime(start_date, "%b. %d, %Y")
            except ValueError:
                donation_date = datetime.datetime.strptime(start_date, "%B %d, %Y")
            donation_date = donation_date.strftime("%Y-%m-%d")
            donation_date_precision = "day"
            try:
                end_date_obj = datetime.datetime.strptime(end_date, "%b. %d, %Y")
            except ValueError:
                end_date_obj = datetime.datetime.strptime(end_date, "%B %d, %Y")
            grant_range = donation_date + " to " + end_date_obj.strftime("%Y-%m-%d")

        amount = date_amount[dollar_loc:].strip().replace("$", "").replace(",", "")

        try:
            locations = list(map(lambda x: x.text.strip(), result.find_all("div", {"class": "geo-focus"})))
        except AttributeError:
            locations = []

        yield {
                "grantee": grantee,
                "url": url,
                "purpose": purpose,
                "donation_date": donation_date,
                "donation_date_precision": donation_date_precision,
                "grant_range": grant_range,
                "amount": amount,
                "locations": locations,
                }


def print_sql(grants_generator):
    insert_stmt = """insert into donations (donor, donee, amount, donation_date, donation_date_precision, donation_date_basis, cause_area, url, donor_cause_area_url, notes, affected_cities) values"""
    first = True
    for grant in grants_generator:
        if first:
            print(insert_stmt)
        notes = ["Purpose: " + grant["purpose"]]
        get_location(grant["locations"])  # TODO remove later
        if grant["grant_range"]:
            notes.append("Grant period: " + grant["grant_range"])
        print(("    " if first else "    ,") + "(" + ",".join([
            mysql_quote("W. K. Kellogg Foundation"),  # donor
            mysql_quote(grant["grantee"]),  # donee
            str(grant["amount"]),  # amount
            mysql_quote(grant["donation_date"]),  # donation_date
            mysql_quote(grant["donation_date_precision"]),  # donation_date_precision
            mysql_quote("donation log" if grant["donation_date"] else ""),  # donation_date_basis
            mysql_quote(""),  # cause_area
            mysql_quote(grant["url"]),  # url
            mysql_quote(""),  # donor_cause_area_url
            mysql_quote("; ".join(notes)),  # notes
            mysql_quote(str(grant["locations"])),  # affected_cities
        ]) + ")")
        first = False
    if not first:
        # If first is still true, that means we printed nothing above,
        # so no need to print the semicolon
        print(";")


if __name__ == "__main__":
    main()

import re

class Parser(object):
    def __init__(self, container):
        self.container = container

    def get_size(self) -> str:
        size = self.container.find("div", {"class":"ads__unit__content__keys"}).div.text
        return size

    def get_price(self) -> str:
        price = self.container.find("div", {"class":"ads__unit__content__keys"}).text
        price = price.splitlines()[2]
        return price

    # Returns the correct area from the address
    def get_area(self) -> str:
        address = self.get_address()
        if "Gamle Oslo" in address: return "Gamle Oslo"
        elif "Ullevål" in address: return "Ullevål"
        elif "Majorstuen" in address: return "Majorstuen"
        elif "Sentrum" in address: return "Sentrum"
        elif "Bjerke" in address: return "Bjerke"
        elif "Sagene" in address: return "Sagene"
        elif "Vinderen" in address: return "Vinderen"
        elif "Helsfyr" in address: return "Helsfyr"
        elif "Bygdøy" in address: return "Bygdøy"
        elif "Ekeberg" in address: return "Ekeberg"
        elif "Manglerud" in address: return "Manglerud"
        elif "Sogn" in address: return "Sogn"
        elif "Grefsen" in address: return "Grefsen"
        elif "Nordstand" in address: return "Nordstand"
        elif "Ullern" in address: return "Ullern"
        elif "Bjerke" in address: return "Bjerke"
        elif "Hellerud" in address: return "Hellerud"
        elif "Lamberseter" in address: return "Lamberseter"
        elif "Østensjø" in address: return "Østensjø"
        elif "Bøler" in address: return "Bøler"
        elif "Furuset" in address: return "Furuset"
        elif "Grorud" in address: return "Grorud"
        elif "Romsås" in address: return "Romsås"
        elif "Søndre Nordstand" in address: return "Søndre Nordstand"
        elif "Stovner" in address: return "Stovner"
        elif "Marka" in address: return "Marka"
        else: return "UNKOWN AREA"

    # Fetches the pure text from html and deletes all empty lines and gets rid of tabs in the beginning of the string
    def get_title(self) -> str:
        title = self.container.find("h2", {"class":"ads__unit__content__title"}).a.text
        title = title.splitlines()[2]
        title = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', title, flags=re.M)
        # Gets rid of last empty lines:
        if re.match(r'^\s*$', title):
            title = filter(lambda x: not re.match(r'^\s*$', x), title)
        title.replace(",", "|").replace(".", "|")
        return title

    def exceptions(self) -> bool:
        title = self.get_title()
        price = self.get_price()
        if "kollektiv" in title: return True
        if "bokollektiv" in title: return True
        if "STUDENTS ONLY" in title: return True
        if "Utleid" in price: return True
        else: return False

    # Fetches the pure text from html and deletes all empty lines
    def get_address(self) -> str:
        address = self.container.find("div", {"class":"ads__unit__content__details"}).text
        address = address.splitlines()[1]
        # Gets rid of last empty lines:
        if re.match(r'^\s*$', address):
            address = filter(lambda x: not re.match(r'^\s*$', x), address)
        address.replace(",", "|").replace(".", "|")
        return address

    # Fetches the link from html tags and adds the domain name
    def get_link(self) -> str:
        return "www.finn.no" + self.container.find("h2", {"class":"ads__unit__content__title"}).a["href"]

    def get_csv_line(self, container, number) -> str:
        return (str(number) + "," + self.get_title() + "," + self.get_address() + "," + self.get_area() + "," + self.get_price() + "," + self.get_size() + "," + self.get_link() + "\n")

    def get_xlsx_line(self, container, number):
        output = [str(number), str(self.get_title()), self.get_address(), self.get_area(), self.price_to_int(), self.size_to_int(), self.get_link()]

        return output

    def price_to_int(self) -> int:
        price = self.get_price()
        price = price.replace(" ", "").replace("kr", "")
        if type(price) == int:
            return int(price)
        else:
            return price
    def size_to_int(self) -> int:
        size = self.get_size()
        size = size.replace(" ", "").replace(" ", "").replace("m²", "")
        if type(size) == int:
            return int(size)
        else:
            return size
    def print_out_answers(self, container, number):
        print(f"======================================================================")
        print(f"NUMBER:      { number }")
        print(f"TITLE:       { self.get_title() }")
        print(f"ADDRESS:     { self.get_address() }")
        print(f"SIZE:        { self.get_size() }")
        print(f"PRICE:       { self.get_price() }")
        print(f"AREA:        { self.get_area() }")
        print(f"LINK:        { self.get_link() }")
        print(f"======================================================================")

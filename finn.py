# Web scraper for apartments in Oslo
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
import os.path
from parser import Parser
from xlsx import Xlsx

class Finn(object):
    def __init__(self, my_url, number, FILENAME):
        self.my_url = my_url
        self.number = number
        self.FILENAME = "apartments.csv"

    def parser(self):
        containers = self.create_containers()
        container = containers[0]
        data = []
        for container in containers:

            parser = Parser(container)
            self.number = self.number + 1

            if parser.exceptions() == False:
                if os.path.isfile(self.FILENAME) == False:
                    self.create_csv_file()
                elif os.path.isfile(self.FILENAME):
                    # parser.print_out_answers(container, self.number)
                    self.save_csv_file(parser.get_csv_line(container, self.number))
                    data.insert(self.number, parser.get_xlsx_line(container, self.number))
                    # xlsx.write_to_xlsx()
        return data
    # Opening up connection, grabbing the page
    def get_html(self):
        uClient = uReq(self.my_url)
        page_html = uClient.read()
        uClient.close()
        return page_html

    def get_self_number(self):
        return self.number

    def create_csv_file(self):
        print("File not exist. Creating file")
        f = open(self.FILENAME, "w")
        headers = "NUMBER, TITLE, ADDRESS, AREA, PRICE, SIZE, LINK" + "\n"
        f.write(headers)
        f.close()

    def save_csv_file(self, output):
        self.FILENAME = "apartments.csv"
        with open('apartments.csv','a') as f:
            f.write(output)
        f.close()

    # Grabs HTML and parses each apartment with soup
    def create_containers(self):
        try:
            page_html = self.get_html()
            page_soup = soup(page_html, "html.parser")
            containers = page_soup.findAll("div", {"class":"ads__unit__content"})
            return containers
        except:
            print("COULDN'T CONNECT TO THE SERVER!")
            create_containers()

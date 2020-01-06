from finn import Finn
from xlsx import Xlsx

class Main(object):
    def __init__(self):

        my_url = "https://www.finn.no/realestate/lettings/search.html?area_from=20&area_to=80&location=0.20061&location=1.20061.20512&location=1.20061.20513&location=1.20061.20509&location=1.20061.20508&price_from=8000&price_to=15000&property_type=1&property_type=3&sort=2"
        my_url2 = "https://www.finn.no/realestate/lettings/search.html?area_from=20&area_to=80&location=0.20061&location=1.20061.20512&location=1.20061.20513&location=1.20061.20509&location=1.20061.20508&page=2&price_from=8000&price_to=15000&property_type=1&property_type=3&sort=2"
        my_url3 = "https://www.finn.no/realestate/lettings/search.html?area_from=20&area_to=80&location=0.20061&location=1.20061.20512&location=1.20061.20513&location=1.20061.20509&location=1.20061.20508&page=3&price_from=8000&price_to=15000&property_type=1&property_type=3&sort=2"
        my_url4 = "https://www.finn.no/realestate/lettings/search.html?area_from=20&area_to=80&location=0.20061&location=1.20061.20512&location=1.20061.20513&location=1.20061.20509&location=1.20061.20508&page=4&price_from=8000&price_to=15000&property_type=1&property_type=3&sort=2"
        # Opening up connection, grabbing the page
        Finn1 = Finn(my_url, 0, "apartments.csv")
        data = Finn1.parser()
        number = Finn1.get_self_number()
        Finn2 = Finn(my_url2, number, "apartments.csv")
        data += Finn2.parser()
        number = Finn2.get_self_number()
        Finn3 = Finn(my_url3, number, "apartments.csv")
        data += Finn3.parser()
        number = Finn3.get_self_number()

        Finn4 = Finn(my_url4, number, "apartments.csv")
        data += Finn4.parser()
        number = Finn4.get_self_number()
        print(f"Web-scraping done! Found: { number } items!")


        xlsx = Xlsx(data, number)
        xlsx.write_to_xlsx()
Main1 = Main()

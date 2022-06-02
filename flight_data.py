from dotenv import load_dotenv
import os
ENDPOINT = "https://tequila-api.kiwi.com"
TEQ_API_KEY = os.getenv("TEQ_API_KEY")


class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

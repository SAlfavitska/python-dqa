from datetime import datetime
import sys
import requests
from utils.constans import FILE_NAME, API_KEY


class NewsFeed:

    def __init__(self):
        self.news = None

    def write_title(self):
        title = self.__class__.__name__
        while len(title) < 25:
            title = title + '_'
        return title

    def write_to_file(self):
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(self.news + '\n' + '\n')
        print(f"The record was successfully added:\n" f"{self.news}")


class News(NewsFeed):
    def __init__(self):
        super().__init__()
        self.message_text = input(f"Please, enter message text: ")
        self.city = input("Please enter the city: ")
        self.publication_day = f"{datetime.now():%d/%m/%Y  %H:%M}"
        self.news = self.write_title() + '\n' + self.message_text + '\n' + self.city + ", " + self.publication_day


class PrivateAd(News):
    def __init__(self):
        super().__init__()
        self.expiration_date = input("Enter the expiration date in the following format DD/MM/YYYY: ")
        self.validate_date()
        self.news = self.write_title() + '\n' + self.message_text + '\n' + \
                    f'Actual until: {self.expiration_date:%d/%m/%Y}, ' + self.count_days_left() + ' days left'

    def validate_date(self):
        try:
            self.expiration_date = datetime.strptime(self.expiration_date, '%d/%m/%Y')
        except ValueError:
            self.expiration_date = input('Incorrect date format, should be "DD/MM/YYYY".'
                                         'Please, try again or enter exit to close the program.')
            if self.expiration_date != "exit":
                self.validate_date()
            else:
                sys.exit()

    def count_days_left(self):
        current_date = datetime.now()
        dates_diff = self.expiration_date - current_date
        if dates_diff.days < 0:
            print(f"Looks like your advertisement already expired. Correct date and try again.")
            sys.exit()
        return str(dates_diff.days)


class Weather(NewsFeed):
    def __init__(self):
        super().__init__()
        self.city = input("Please enter the city: ")
        self.URL = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&units=metric&lang=en&mode=json&appid={API_KEY}'
        self.response = requests.get(self.URL)
        self.weather = self.response.json()
        self.news = self.write_title() + '\n' + self.weather_response_format()

    def write_title(self):
        title = f'{self.__class__.__name__} in {self.city}'
        while len(title) < 25:
            title = title + '_'
        return title

    def weather_response_format(self):
        try:
            degree = u'\N{DEGREE SIGN}'
            main_data = self.weather['main']
            temperature = main_data['temp']
            humidity = main_data['humidity']
            temp_min = main_data['temp_min']
            temp_max = main_data['temp_max']
            wind_speed = self.weather['wind']['speed']
            report = self.weather['weather']
            city_weather = f"Temperature: {int(temperature)}{degree}C\n" f"Humidity: {humidity}%\n" \
                       f"Temp_min: {temp_min}{degree}C\n" f"Temp_max: {temp_max}{degree}C\n" \
                       f"Wind speed: {wind_speed} meter/sec\n" f"Weather Report: {report[0]['description']}"
            return city_weather
        except KeyError:
            print('The city name is incorrect.')
            sys.exit()


def main():
    choice = input("What to you wand to add? (To exit, please enter any other input.)" + "\n"
                        + "1- News, 2 - Private Advertising, 3- Weather." + "\n")
    if choice == '1':
        News().write_to_file()
    elif choice == '2':
        PrivateAd().write_to_file()
    elif choice == '3':
        Weather().write_to_file()
    else:
        print("Try again!")


def repetition():
    while True:
        answer = input("Run again? (y/n): ")
        if answer not in ('y', 'n'):
            print("Invalid input.")
            sys.exit()
        if answer == 'y':
            main()
        else:
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
    repetition()

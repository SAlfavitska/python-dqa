from datetime import datetime
import sys


class NewsFeed:

    def __init__(self, message_text):
        self.message_text = message_text
        self.news = None

    def write_title(self):
        title = self.__class__.__name__
        while len(title) < 25:
            title = title + '-'
        return title

    def write_to_file(self):
        with open('news_feed.txt', "a", encoding="utf-8") as file:
            file.write(self.news + '\n' + '\n')
        print(f"The record was successfully added:\n" f"{self.news}")


class News(NewsFeed):
    def __str__(self):
        return self.news

    def __init__(self, message_text, city):
        self.city = city
        super().__init__(message_text)
        self.publication_day = f"{datetime.now():%d/%m/%Y  %H:%M}"
        self.news = self.write_title() + '\n' + self.message_text + '\n' + self.city + ", " + self.publication_day


class PrivateAd(NewsFeed):
    def __str__(self):
        return self.news

    def __init__(self, message_text, expiration_date):
        self.expiration_date = expiration_date
        super().__init__(message_text)
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


class Quote(NewsFeed):
    def __str__(self):
        return self.news

    def __init__(self, message_text, author):
        self.author = author
        super().__init__(message_text)
        self.publication_day = f"{datetime.now():%d/%m/%Y  %H:%M}"
        self.news = self.write_title() + '\n' + f'{self.message_text} - {self.author}'
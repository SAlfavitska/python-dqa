from datetime import datetime
import sys
import os
from strings_HW_3.strings_homework_3_review import correct_letters_case


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


class FileData:
    def __str__(self):
        return self.text_to_append

    def __init__(self, data):
        self.file_content = data
        self.text_to_append = ''
        self.parce_file()

    @staticmethod
    def validate_record_type(record_type):
        if record_type not in ('News', 'Privatead', 'Quote'):
            print(f'Unsupported self type {record_type} in the file, exiting the program')
            sys.exit()

    @staticmethod
    def validate_elements_num(record_elements):
        if len(record_elements) != 3:
            print(f'{record_elements} should consists of 3 elements separated by |. Exiting.')
            sys.exit()

    @staticmethod
    def normalize_list(record_elements):
        for i in range(len(record_elements)):
            record_elements[i] = correct_letters_case(record_elements[i])
        return record_elements

    @staticmethod
    def add_empty_rows_below(text):
        return text + '\n' + '\n'

    def parce_file(self):
        for row in self.file_content.split('\n'):
            record_elements = self.normalize_list(row.split(' | '))
            self.validate_elements_num(record_elements)
            self.validate_record_type(record_elements[0])
            if record_elements[0] == 'News':
                obj = News(record_elements[1], record_elements[2])
                self.text_to_append += self.add_empty_rows_below(str(obj))
            elif record_elements[0] == 'Privatead':
                obj = PrivateAd(record_elements[1], record_elements[2])
                self.text_to_append += self.add_empty_rows_below(str(obj))
            elif record_elements[0] == 'Quote':
                obj = Quote(record_elements[1], record_elements[2])
                self.text_to_append += self.add_empty_rows_below(str(obj))


class Choose:

    def __init__(self):
        self.input_type = input("""Choose input type:
                                1 - Input
                                2 - Load from file
                                3 - Exit
    """)
        if self.input_type == '1':
            self.type_of_publication = input(f"""Choose type of news or exit, please (Enter digit):
                                1 - News
                                2 - Private Ad
                                3 - Quote
                                4 - Exit
    """)
        elif self.input_type == '2':
            self.folder_choose = input(f"""Folder for file:
                                1 - Default Folder
                                2 - User folder
    """)
            if self.folder_choose == '1':
                self.default_path = sys.path[1]
            elif self.folder_choose == '2':
                self.file_path = input(r"Enter path to file (in format C:\) ")
            self.source_file_name = input('Enter your file name\n')
        elif self.input_type == '3':
            sys.exit()

    @staticmethod
    def read_file(file_path, source_file_name):
        try:
            with open(f'{file_path}\\{source_file_name}', "r+") as file:
                return file.read()
        except IOError:
            print(f'File {file_path}\\{source_file_name} was not found!')
            sys.exit()

    @staticmethod
    def to_file(text):
        with open('news_feed.txt', 'a', encoding="utf-8") as f:
            f.write(text)
        print(text + 'Was added')

    @staticmethod
    def delete_source_file(path, source_file_name):
        path = os.path.join(path, source_file_name)
        os.remove(path)
        print(f"{source_file_name} has been removed successfully.")

    @staticmethod
    def news():
        text = input('Please, enter message text: ')
        city = input('Please, enter the city: ')
        return News(text, city).write_to_file()

    @staticmethod
    def privatead():
        text = input('Please, enter message text: ')
        expiration_date = input('Enter the expiration date in the following format DD/MM/YYYY: ')
        return PrivateAd(text, expiration_date).write_to_file()

    @staticmethod
    def quote():
        quote = input('Please, enter the quote: ')
        author = input('Please, enter the author ')
        return Quote(quote, author).write_to_file()


if __name__ == '__main__':
    source_file_name = 'input_file.txt'
    while True:
        user_choose = Choose()
        if user_choose.input_type == '1':
            if user_choose.type_of_publication == '1':
                user_choose.news()
            elif user_choose.type_of_publication == '2':
                user_choose.privatead()
            elif user_choose.type_of_publication == '3':
                user_choose.quote()
        elif user_choose.input_type == '2':
            if user_choose.folder_choose == '1':
                file_path = user_choose.default_path
                print(file_path)
                file_content = user_choose.read_file(file_path, source_file_name)
                file_data = FileData(file_content)
                user_choose.to_file(str(file_data))
                user_choose.delete_source_file(file_path, source_file_name)
            elif user_choose.folder_choose == '2':
                file_path = user_choose.file_path
                print(file_path)
                file_content = user_choose.read_file(file_path, source_file_name)
                file_data = FileData(file_content)
                user_choose.to_file(str(file_data))
                user_choose.delete_source_file(file_path, source_file_name)

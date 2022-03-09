import sys
from publications import News, PrivateAd, Quote
import os
import json


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
            self.file_type = input("""Choose type of file:
                                            1 - TXT
                                            2 - JSON
    """)

            if self.folder_choose == '1':
                self.file_path = sys.path[1]
            elif self.folder_choose == '2':
                self.file_path = input(r"Enter path to file (in format C:\) ")
            self.source_file_name = input('Enter your file name\n')
        elif self.input_type == '3':
            sys.exit()

    def json_to_list(self):
        with open(f'{self.file_path}\\{self.source_file_name}') as json_file:
            json_list = json.load(json_file)
        return json_list

    def read_txt_file(self):
        try:
            with open(f'{self.file_path}\\{self.source_file_name}', "r+") as file:
                return file.read()
        except IOError:
            print(f'File {self.file_path}\\{self.source_file_name} was not found!')
            sys.exit()

    @staticmethod
    def to_file(text):
        with open('News_feed.txt', 'a', encoding="utf-8") as f:
            f.write(text)
        print(text + 'Was added')

    def delete_source_file(self):
        os.remove(self.source_file_name)
        print(f"{self.source_file_name} has been removed successfully.")

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

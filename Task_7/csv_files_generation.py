import csv
import pandas as pd
import regex as re

csv_1_name = '1_word_count.csv'
csv_2_name = '2_letters_stat.csv'


def sort_csv(csv_name, column_name):
    df = pd.read_csv(csv_name)
    sorted_df = df.sort_values(column_name)
    sorted_df.to_csv(csv_name, index=False)


class CSVFile:
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name
        words_dict = self.word_count()
        self.create_words_csv(words_dict)
        letters_list = self.create_letters_list(self.file_name)
        count_of_letters = self.create_letters_count_list(letters_list)
        self.create_stat_csv(count_of_letters)
        print(f'Files {csv_1_name} and {csv_2_name} were created.')

    def word_count(self):
        word_pattern = r"\p{L}+"
        with open(f'{self.file_path}\\{self.file_name}') as text_file:
            words_dict = {}
            words = re.findall(word_pattern, text_file.read().lower())
            for word in words:
                if word not in words_dict.keys():
                    words_dict[word] = 1
                elif word in words_dict.keys():
                    words_dict[word] += 1
        return words_dict

    @staticmethod
    def create_words_csv(words_dict):
        with open(csv_1_name, 'w', newline='') as csv_words:
            header = ['Word', 'Repeat_amount']
            writer = csv.DictWriter(csv_words, fieldnames=header)
            writer.writeheader()
            for key, value in words_dict.items():
                writer.writerow({'Word': key, 'Repeat_amount': value})
        sort_csv(csv_1_name, 'Word')

    @staticmethod
    def create_letters_list(text_file):
        letter_pattern = r"\p{L}"
        letters = list()
        with open(text_file, 'r') as file:
            text = file.read()
            for lt in re.findall(letter_pattern, text):
                letters.append(lt)
        return letters

    @staticmethod
    def create_letters_count_list(letters_list):
        count_of_letters = []
        letters_list_len = len(letters_list)
        for el in letters_list:
            lwr = letters_list.count(el.lower())
            uppr = letters_list.count(el.upper())
            psntg = round(((lwr + uppr) / letters_list_len) * 100, 3)
            count_of_letters.append((el.lower(), lwr + uppr, uppr, psntg))
        count_of_letters = list(dict.fromkeys(count_of_letters))
        return count_of_letters

    @staticmethod
    def create_stat_csv(count_of_letters):
        with open(csv_2_name, 'w', newline='') as csv_stat:
            header = ['Letter', 'Count_all', 'Count_uppercase', 'Percentage %']
            writer = csv.DictWriter(csv_stat, fieldnames=header)
            writer.writeheader()
            for ltr, lwr, upr, psntg in count_of_letters:
                writer.writerow({'Letter': ltr, 'Count_all': lwr, 'Count_uppercase': upr, 'Percentage %': psntg})
        sort_csv(csv_2_name, 'Letter')
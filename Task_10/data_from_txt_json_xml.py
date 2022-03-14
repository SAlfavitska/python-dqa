import sys
from string_normalization import correct_letters_case
from publications import News, PrivateAd, Quote
sys.path.append('/')


class FileData:
    def __str__(self):
        return self.text_to_append

    def __init__(self, data, file_type):
        self.file_content = data
        self.text_to_append = ''
        if file_type == 'f':
            self.parce_file()
        elif file_type in ('j', 'x'):
            self.parce_list_to_file()

    @staticmethod
    def validate_record_type(record_type):
        if record_type not in ('News', 'Privatead', 'Quote'):
            print(f'Unsupported record {record_type} in the file, exiting the program')
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

    def parce_list_to_file(self):
        for element in self.file_content:
            try:
                if element['type'] == 'News':
                    obj = News(element['text'], element['city'])
                    self.text_to_append += self.add_empty_rows_below(str(obj))
                elif element['type'] == 'PrivateAd':
                    obj = PrivateAd(element['text'], element['valid_until'])
                    self.text_to_append += self.add_empty_rows_below(str(obj))
                elif element['type'] == 'Quote':
                    obj = Quote(element['text'], element['author'])
                    self.text_to_append += self.add_empty_rows_below(str(obj))
            except KeyError:
                print("Please, check JSON structure and field names.")
                sys.exit()

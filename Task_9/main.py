import os
from choose import Choose
from data_from_txt_json_xml import FileData
from csv_files_generation import CSVFile


def main():
    while True:
        user_choose = Choose()
        file_path = os.path.dirname(os.path.abspath(__file__))
        file_name = 'News_feed.txt'
        if user_choose.input_type == '1':
            if user_choose.type_of_publication == '1':
                user_choose.news()
            elif user_choose.type_of_publication == '2':
                user_choose.privatead()
            elif user_choose.type_of_publication == '3':
                user_choose.quote()
        elif user_choose.input_type == '2':
            if user_choose.file_type == '1':
                file_content = user_choose.read_txt_file()
                file_data = FileData(file_content, 'f')
                user_choose.to_file(str(file_data))
                # user_choose.delete_source_file()
            elif user_choose.file_type == '2':
                json_list = user_choose.json_to_list()
                file_data = FileData(json_list, 'j')
                user_choose.to_file(str(file_data))
                # user_choose.delete_source_file()
            elif user_choose.file_type == '3':
                xml_list = user_choose.xml_to_list()
                file_data = FileData(xml_list, 'j')
                user_choose.to_file(str(file_data))
                # user_choose.delete_source_file()
        CSVFile(file_path, file_name)


if __name__ == '__main__':
    main()

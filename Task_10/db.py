import sqlite3
import os

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "module_10.db")


class DB:
    def __init__(self, row, news_type):
        self.row = row
        self.news_type = news_type
        self.conn = sqlite3.connect(db_path)
        self.tables_metadata = ['News', "Text", "City", "Publication_Time"], \
                               ['PrivateAd', "Text", "Expiration_date", "Days_left"], \
                               ['Quote', "Text", "Author", "Publication_Time"]
        self.create_tables()
        self.write_row_to_table()

    def create_tables(self):
        for table_metadata in self.tables_metadata:
            with self.conn as con:
                cursor = con.cursor()
                cursor.execute('pragma encoding')
                cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_metadata[0]} '
                               f'{table_metadata[1], table_metadata[2], table_metadata[3]};')

    def write_row_to_table(self):
        with self.conn as con:
            cursor = con.cursor()
            cursor.execute(f'WITH cte(c1, c2, c3) AS (SELECT * FROM {self.news_type}) '
                           f'SELECT * FROM cte WHERE c1 = \'{self.row[0]}\' '
                           f'AND c2 = \'{self.row[1]}\' ')
            row_num = cursor.fetchone()
            if row_num is not None:
                print(f'Duplicated row in table {self.news_type} with values'
                      f'\'{self.row[0]}\', \'{self.row[1]}\'')
            else:
                cursor.execute(f'INSERT INTO {self.news_type} VALUES (\'{self.row[0]}\''
                               f',\'{self.row[1]}\''
                               f',\'{self.row[2]}\');')
                self.conn.commit()

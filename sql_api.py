import mysql.connector as sql
import json

class sql_api:
    def __init__(self, password : str ,host : str = 'localhost', user : str = 'root') -> None:
        '''
        API to fetch data from sql table and convert it into various format (json, txt, csv) to be used in pandas library for data analysis
        '''
        self.host = host
        self.user = user
        self.password = password
        self.conector = sql.connect(host = self.host, user = self.user, passwd = self.password)
        self.cursor = self.conector.cursor()

    def get_json_all(self, database : str) -> None:
        '''
        Convert all tables present in the specified database into JSON file with same name as the table name.
        '''
        try:
            self.cursor.execute(f'use {database};')
        except:
            raise Exception('no such database was found')
        
        self.cursor.execute("show tables;")
        result = self.cursor.fetchall()
        tables = [row[0] for row in result]
        self.get_json(database, *tables)

    def get_json(self, database : str, *tables : str) -> None:
        '''Convert only specified tables present in the specified database into JSON file with same name as the table name
        '''
        try:
            self.cursor.execute(f'use {database};')
        except:
            raise Exception('no such database was found')
        try:
            for table in tables:
                with open(f'{table}.json', 'w') as json_file:
                    json.dump(self.get_dict_data(database, table), json_file)
        except:
            raise Exception('no such table was found')        
    
    def get_dict_data(self, database: str, table : str) -> dict:
        '''
        Return the table specified in a Dictionary format. Database needs to be specified.
        '''
        self.cursor.execute(f'use {database}')
        self.cursor.execute(f'desc {table};')
        result = self.cursor.fetchall()
        tables_row_number = len(result)
        fields = [row[0] for row in result]
        self.cursor.execute(f'select * from {table};')
        result = self.cursor.fetchall()
        return {fields[col] : {str(row) : result[row][col] for row in range(len(result))} for col in range(tables_row_number)}


    def get_csv_all(self, database : str) -> None:
        '''
        Convert all tables present in the specified database into CSV file with same name as the table name.
        '''
        

    def get_csv(self, datbase : str, *table : str) -> None:
        '''
        Convert only specified tables present in the specified database into CSV file with same name as the table name. 
        '''
    
    def get_list__data(self, databse : str, *tables : str) -> None:
        '''Return the table specified in a Nested List format. Database needs to be specified.
        '''


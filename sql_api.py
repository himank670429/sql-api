import mysql.connector as sql
import json
import csv

class sql_api:
    def __init__(self,host : str, user : str,  password : str ) -> None:
        '''
        API to fetch data from sql table and convert it into various format (json, txt, csv) to be used in pandas library for data analysis
        '''
        self.host = host
        self.user = user
        self.password = password
        try:
            self.conector = sql.connect(host = self.host, user = self.user, passwd = self.password)
            self.cursor = self.conector.cursor()
        except:
            raise Exception("cannot connect to the database!!")

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
                    json.dump(self.read_data(database, table), json_file)

        except:
            raise Exception('no such table was found')        
    
    def get_csv_all(self, database : str) -> None:
        '''
        Convert all tables present in the specified database into CSV file with same name as the table name.
        '''
        try:
            self.cursor.execute(f'use {database};')
        except:
            raise Exception('no such database was found')

        self.cursor.execute("show tables;")
        result = self.cursor.fetchall()
        tables = [row[0] for row in result]
        self.get_csv(database, *tables)

    def get_csv(self, database : str, *tables : str) -> None:
        '''
        Convert only specified tables present in the specified database into CSV file with same name as the table name. 
        '''
        try:
            self.cursor.execute(f'use {database};')
        except:
            raise Exception('no such database was found')
        try:
            for table in tables:
                with open(f'{table}.csv', 'w', newline = "") as csv_file:
                    writer = csv.writer(csv_file)
                    self.cursor.execute(f"desc {table};")
                    result = self.cursor.fetchall()
                    writer.writerow([row[0] for row in result])

                    self.cursor.execute(f'select * from {table};')
                    result = self.cursor.fetchall()
                    writer.writerows(result)    
        except:
            raise Exception('no such table was found')  
    
    def read_data(self, database: str, table : str) -> dict:
        '''
        Return the table specified in a Dictionary format to be read into pandas DataFrame.
        '''
        self.cursor.execute(f'use {database}')
        self.cursor.execute(f'desc {table};')
        result = self.cursor.fetchall()
        tables_row_number = len(result)
        fields = [row[0] for row in result]
        self.cursor.execute(f'select * from {table};')
        result = self.cursor.fetchall()
        return {fields[col] : {str(row) : result[row][col] for row in range(len(result))} for col in range(tables_row_number)}
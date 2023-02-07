# SQL API
This **API** lets you get get the data from your local MySQL database in the form of either **CSV** or **JSON** or a **Python Dictionary**.

---

### Installation of for SQL API
* You need to install Python/MySql connector in you mysql database.

* Once that is done, run this command in your terminal.
    ```zsh
    pip install mysql.connector
    ```
* Now download this api by cloning this repository to your local machine by typing the following command in you terminal
    ```zsh
    git clone https://github.com/himank670429/sql-api.git
    ```
    make sure to clone this repository in your current working project folder.

---

### How To use
* Importing the API
    ```python 
    from sql_api import sql_api
    ```
* Initiallize the class object
    ```python
    from sql_api import sql_api 
    api = sql_api(host = "{YOUR_HOST}", user = "{YOUR_USER}", password = "{YOUR_MYSQL_PASSOWRD}")
    ```
* Methods
    1. **get_json_all(database)** :- Convert all tables present in the specified database into JSON file with same name as the table name.
    The converted JSON file is saved in the current working directory.
        ```python
        from sql_api import sql_api
        api = sql_api(host = "{YOUR_HOST}", user = "{YOUR_USER}", password = "{YOUR_MYSQL_PASSOWRD}")

        api.get_json_all("DATABASE_NAME")
        ```

    2. **get_json(database, \*tables)** :- Convert only specified tables present in the specified database into JSON file with same name as the table name.
    The converted JSON file is saved in the current working directory.
        ```python
        from sql_api import sql_api
        api = sql_api(host = "{YOUR_HOST}", user = "{YOUR_USER}", password = "{YOUR_MYSQL_PASSOWRD}")

        api.get_json("DATABASE_NAME", "TABLE_1", "TABLE_2",...,"TABLE_N")
        ```

    3. **get_csv_all(database)** :- Convert all tables present in the specified database into CSV file with same name as the table name.
    The converted CSV file is saved in the current working directory.
        ```python
        from sql_api import sql_api
        api = sql_api(host = "{YOUR_HOST}", user = "{YOUR_USER}", password = "{YOUR_MYSQL_PASSOWRD}")

        api.get_csv_all("DATABASE_NAME")
        ```

    4. **get_csv(database, \*tables)** :- Convert only specified tables present in the specified database into CSV file with same name as the table name.
    The converted CSV file is saved in the current working directory.
        ```python
        from sql_api import sql_api
        api = sql_api(host = "{YOUR_HOST}", user = "{YOUR_USER}", password = "{YOUR_MYSQL_PASSOWRD}")

        api.get_csv("DATABASE_NAME", "TABLE_1", "TABLE_2",...,"TABLE_N")
        ```

    5. **read_data(database, table)** :- Return the table specified in a Dictionary format to be read into pandas DataFrame. Database needs to be specified.
        ```python
        from sql_api import sql_api
        api = sql_api(host = "{YOUR_HOST}", user = "{YOUR_USER}", password = "{YOUR_MYSQL_PASSOWRD}")

        data = api.get_data_dict("DATABASE_NAME", "TABLE_NAME")
        print(data) 

        # or further use it in pandas

        import pandas as pd
        df = pd.DataFrame(data)
        print(df)
        ```

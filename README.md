# SQL API
This **API** lets you extract table data from **SQL databse** into **json/csv** files to be used as DataFrame with **pandas** for **Data Analysis**.

This **API** also lets you lets you Extract the Table data to be directly used up in into you code that is no external files. 

You need `mysql.connector` in order to use this api

---

### Installation of for SQL API
* you need to install Python/MySql connector in you mysql database.

* once that is done, run this command in your terminal.
    ```zsh
    pip install mysql.connector
    ```
* now download this api by cloning this repository to your local machine by typing the following command in you terminal
    ```zsh
    git clone https://github.com/himank670429/sql-api.git
    ```
    make sure to clone this repository in your current working project folder.

---

### How To use
* importing the API
    ```python 
    from sql_api import sql_api
    ```
* Initiallize the class object
    ```python
    from sql_api import sql_api
    api = sql_api(password = "YOUR MYSQL PASSWORD")
    ```
    here `host` and `user` have default value of `localhost` and `root` respectively. but you can specify them as keyword argument as follows

    ```python 
    api = sql_api(host = "YOUR HOST", user = "YOU USER", password = "YOUR MYSQL PASSOWRD")

    ```
* Methods
    1. **get_json_all(database)** :- Convert all tables present in the specified database into JSON file with same name as the table name.
    The converted JSON file is saved in the current working directory.
        ```python
        from sql_api import sql_api
        api = sql_api(host = "YOUR HOST", user = "YOU USER", password = "YOUR MYSQL PASSOWRD")

        api.get_json_all("DATABASE_NAME")
        ```
    2. **get_json(database, \*tables)** :- Convert only specified tables present in the specified database into JSON file with same name as the table name.
    The converted JSON file is saved in the current working directory.
        ```python
        from sql_api import sql_api
        api = sql_api(host = "YOUR HOST", user = "YOU USER", password = "YOUR MYSQL PASSOWRD")

        api.get_json("DATABASE_NAME", "TABLE_1", "TABLE_2",...,"TABLE_N")
        ```
    
    3. **get_data_dict(database, table)** :- Return the table specified in a Dictionary format. Database needs to be specified.
        ```python
        from sql_api import sql_api
        api = sql_api(host = "YOUR HOST", user = "YOU USER", password = "YOUR MYSQL PASSOWRD")

        data = api.get_data_dict("DATABASE_NAME", "TABLE_NAME")
        print(data) 

        # or further use it in pandas

        import pandas as pd
        df = pd.DataFrame(data)
        print(df)
        ```
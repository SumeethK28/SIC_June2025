import pymysql
import sys as s
from tabulate import tabulate

connection = None    # calling it globally so that every function can access it 

def connect_db():
    global connection
    if not connection:    # Checks if already connection is made 
        try:
            connection = pymysql.Connect(host = "localhost", 
                                        user = "root", 
                                        password = "root123", database = "sumeeth_db", port = 3306, 
                                        charset = "utf8")
            print("Connection Successful")
        except Exception as e:
            print("ConnectionError: Database Connection Failed")
            print(e)
    else:
        print("Connection already done")

def disconnect_db():
    global connection
    if connection:     # checks if connection is made and has to be disconnected 
        try:
            connection.close()
            print("Disconnected Successfully")
            connection = None
        except Exception as e:
            print("ConnectionError: Could not Disconnect")
            print(e)
    else:
        print("No Active Connection to Disconnect")

def create_db():
    global connection
    if not connection:   # checks if it is disconnected, if yes then it prints an error message
        print("Not connected to Database")
        return
    try:
        cursor = connection.cursor()
        result = cursor.execute("show databases like 'sumeeth_db'")   # checks if database already exists, if yes then it wont try to execute the create query itself
        if result:
            print("Database already exists")
        else:
            query = "create database sumeeth_db"
            cursor.execute(query)
            print("Database Created")
        cursor.close()
    except Exception as e:
        print("CreationError: Error in Creation")
        print(e)

def create_table():
    global connection
    if not connection:   # checks if it is disconnected, if yes then it prints an error message
        print("Not connected to Database")
        return
    try:
        cursor = connection.cursor()
        result = cursor.execute("show tables like 'employees'")   # checks if table already exists, if yes then it wont try to execute the create query itself
        if result:
            print("Table already exists")
        else:
            query = '''create table employees(
                    id int primary key auto_increment, 
                    name varchar(50) not null, 
                    designation varchar(30), 
                    phone_number bigint unique, 
                    salary float, 
                    commission float default(0), 
                    years_of_experience tinyint, 
                    technology varchar(30) not null)
                    '''
            cursor.execute(query)
            print('Table created')
        cursor.close()
    except Exception as e:
        print('CreationError: Error in Creation')
        print(e)

def get_next_id_available():
    query = """                       
        SELECT COALESCE(MIN(t1.id + 1), 1) AS next_id
        FROM employees t1
        LEFT JOIN employees t2 ON t1.id + 1 = t2.id
        WHERE t2.id IS NULL
    """
    cursor = connection.cursor()
    cursor.execute(query)   # This query is used to find out what is the next id number by finding missing values
    next_id = cursor.fetchone()[0]  # In case we have multiply values we consider the first one as the id number 
    cursor.close()
    return next_id

def insert_data():
    global connection
    if not connection:
        print("Not connected to Database")
        return
    
    next_id = get_next_id_available()

    lst = list(map(str, input("Enter columns names you want to insert the data in the table with white spaces between each name (including id): ").split()))

    lst1 = list(map(str, input("Enter values of that names you want to insert the data in the table with commas between each value: ").split(",")))

    columns = ", ".join(lst)    # Actual names are given to query so converted to string
    placeholders = ", ".join(['%s'] * (len(lst1) + 1))   # a command is sent to sql driver "we will send the actual values later, instead we provide formats (%s) in place of it" to avoid sql injection
    values = [next_id] + lst1  # Converting next_id variable to list and lst1 list to that newly created list 

    query = f"insert into employees ({columns}) values ({placeholders})"

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print("Data has been inserted successfully")
        cursor.close()
    except Exception as e:
        print("InsertionError: Failed to insert data into table")
        print(e)

def read_all_data():
    global connection
    if not connection:   # checks if it is disconnected, if yes then it prints an error message
        print("Not connected to Database")
        return
    query1 = "select * from employees"
    query2 = "select column_name from information_schema.columns where table_name = 'employees' and table_schema = 'sumeeth_db'"
    try:
        cursor = connection.cursor()

        cursor.execute(query1)
        rows = cursor.fetchall()

        cursor.execute(query2)
        columns = cursor.fetchall()
        header = []
        for column in columns:
            data = "%s" % column
            header.append(data.upper())

        print(tabulate(rows, headers = header, tablefmt = "rounded_grid", missingval = "N/A",numalign = "center", stralign = "center"))
        print("All rows retrived")
        cursor.close()
    except Exception as e:
        print("RetrivalError: Could not retrive rows from Database")
        print(e)

def exit_program():
    disconnect_db()    # In case if the user directly exists the program without disconnecting, then here it will be disconnected
    s.exit('End of program')

def invalid_choice():
    print('Invalid Choice entered')

if __name__ == "__main__":
    menu = {
        1: connect_db,
        2: create_db,
        3: create_table,
        4: read_all_data,
        5: insert_data,
        6: disconnect_db,
        7: exit_program
    }

    while True:
        print("1. Connect   2. Create Database   3. Create Table   4. Display Table Contents   5. Insert   6. Disconnect   7. Exit")
        try:
            choice = int(input("Enter your choice: "))
            menu.get(choice, invalid_choice) ()
        except ValueError:
            print("Please enter a valid number.")   # If in case nothing is entered
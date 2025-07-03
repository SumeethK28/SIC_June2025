import pymysql
import sys as s

connection = None    # calling it globally so that every function can access it 

def connect_db():
    global connection
    if not connection:    # Checks if already connection is made 
        try:
            connection = pymysql.Connect(host = "localhost", 
                                        user = "root", 
                                        password = "sumit@2814", database = "sumeeth_db", port = 3306, 
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

def read_all_data():
    global connection
    if not connection:   # checks if it is disconnected, if yes then it prints an error message
        print("Not connected to Database")
        return
    query = "select * from employees"
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
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
        5: disconnect_db,
        6: exit_program
    }

    while True:
        print("1. Connect   2. Create Database   3. Create Table   4. Display Table Contents   5. Disconnect   6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            menu.get(choice, invalid_choice) ()
        except ValueError:
            print("Please enter a valid number.")   # If in case nothing is entered
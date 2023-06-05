import pyodbc
import time


    
# Get connection details from config file
def get_connection_info(file_name: str) -> dict:
    # Initial empty dictionary to store connection details
    connections = {}

    # Open config file to get connection info
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            # remove all white space (space, tab, new line)
            line = ''.join(line.split())

            # get connection info
            connection_param, connection_value = line.split(":")
            connections[connection_param] = connection_value
    return connections

# Find first 10 people in the database based on their lexicographical order
def find_first_on_name(connection: dict):
    cursor = connection.cursor()
    sql = "SELECT Name,Phone,Age FROM Demo.Person_SQL " \
          "ORDER BY Name"
    print("Name\tPhone\tAge")

    rows = cursor.execute(sql)
    for row in rows:
        for item in row:
            print("{}\t".format(item), end='')
        print("")
    

# Create person table
def create_person_table(connection: dict) -> None:
    cursor = connection.cursor()
    create_table = "CREATE TABLE Demo.Person_SQL(Name varchar(50) unique, Phone varchar(50), Age int)"
    try:
        cursor.execute(create_table)
        print("Created Demo.Person_SQL table successfully.")
        connection.commit()
    except Exception as e:
        print("Error creating person: " + str(e))
        
# Add item to person
def add_person_item(connection: dict, name: str, phone: str, age: int) -> None:
    try:
        t = time.process_time()
        sql = "INSERT INTO Demo.Person_SQL (Name,Phone,Age) VALUES (?,?,?)"
        cursor = connection.cursor()
        cursor.execute(sql, name, phone, int(age))
        print("Added new line item for Person_SQL: {}.".format(name))
        connection.commit()
        elapsed_time = time.process_time() - t
        print("Time took to execute(SQL): " + str(elapsed_time))
    except Exception as e:
        print("Error adding to person: " + str(e))
        
# Update item in person table
def update_person_item(connection: dict, name: str, phone: str, age: int) -> None:
    t = time.process_time()
    sql = "UPDATE Demo.Person_SQL SET Phone = ?, Age= ? WHERE Name= ?"
    cursor = connection.cursor()
    cursor.execute(sql, phone, int(age), name)
    if cursor.rowcount > 0:
        print("Updated {} successfully.".format(name))
    else:
        print("{} does not exist.".format(name))
    connection.commit()
    elapsed_time = time.process_time() - t
    print("Time took to execute(SQL): " + str(elapsed_time))

# Delete item from person
def delete_person_table(connection, name):
    t = time.process_time()
    sql = "DELETE FROM Demo.Person_SQL WHERE name = ?"
    cursor = connection.cursor()
    cursor.execute(sql, name)
    if cursor.rowcount > 0:
        print("Deleted {} successfully.".format(name))
    else:
        print("{} does not exist.".format(name))
    connection.commit()
    elapsed_time = time.process_time() - t
    print("Time took to execute(SQL): " + str(elapsed_time))

# Task 2: Create Person Table
def task_create_person(connection: dict) -> None:
    print("Create person")
    create_person_table(connection)

# Task 3: Add item to Person table
# Note: Choose person name using list of persons generated by Task 2
def task_add_to_person(connection: dict) -> None:
    print("Add to person")
    name = input("Name: ")
    phone = input("Phone: ")
    age = input("Age: ")
    add_person_item(connection, name, phone, age)

# Task 4: Update item in Person table
def task_update_person(connection: dict) -> None:
    print("Update person info")
    name = input("What is the name of the person that you wish to update: ")
    phone = input("New Phone #: ")
    age = input("New Age: ")
    update_person_item(connection, name, phone, age)

# Task 5: Delete item from Person table
def task_delete_person(connection: dict) -> None:
    print("Delete from person")
    name = input("Which person you want to delete? ")
    delete_person_table(connection, name)

# Execute task based on user input
def execute_selection(selection: int, connection: dict) -> None:
    if selection == 1:
        find_first_on_name(connection)
    elif selection == 2:
        task_create_person(connection)
    elif selection == 3:
        task_add_to_person(connection)
    elif selection == 4:
        task_update_person(connection)
    elif selection == 5:
        task_delete_person(connection)
        
def run() -> None:
    # Retrieve connection information from configuration file
    connection_detail = get_connection_info("connection.config")

    ip = connection_detail["ip"]
    port = int(connection_detail["port"])
    namespace = connection_detail["namespace"]
    username = connection_detail["username"]
    password = connection_detail["password"]
    driver = "{InterSystems IRIS ODBC35}"
    
    # Create connection to InterSystems IRIS using pyodbc
    connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}' \
    .format(driver, ip, port, namespace, username, password)
    connection_pyodbc = pyodbc.connect(connection_string)
    connection_pyodbc.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    connection_pyodbc.setencoding(encoding='utf-8')
    print("Connected to InterSystems IRIS using pyodbc")

    # Starting interactive prompt
    while True:
        print("1. View First 10")
        print("2. Create Person Table")
        print("3. Add Person data")
        print("4. Update Person data")        
        print("5. Delete Person Data")
        print("6. Quit")
        selection = int(input("What would you like to do? "))
        if selection == 6:
            break
        elif selection not in range(1, 7):
            print("Invalid option. Try again!")
            continue
        execute_selection(selection, connection_pyodbc)

if __name__ == '__main__':
    run()

import pyodbc


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
        print("1. Test")
        print("2. Store Person data")
        print("3. View Person data")
        print("4. Delete Person Data")
        print("5. Quit")
        selection = int(input("What would you like to do? "))
        if selection == 5:
            break
        elif selection not in range(1, 6):
            print("Invalid option. Try again!")
            continue


if __name__ == '__main__':
    run()

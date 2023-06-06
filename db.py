import iris
import time

# view globals in database
def view_globals(iris_obj: iris.IRIS) -> None:
    size = iris_obj.get("^Demo.PersonD")
    for i in range(size):
        globalBytes = iris_obj.getBytes("^Demo.PersonD", i + 1)
        list = iris.IRISList(globalBytes)
        print(list.get(2), list.get(3), list.get(4))

# add an entry into the database based on given [properties]
def store_global(iris_obj: iris.IRIS, properties: list) -> None:
    t = time.process_time()
    index = iris_obj.get("^Demo.PersonD") + 1
    list = iris.IRISList()
    for property in properties: list.add(property)
    iris_obj.set(list, "^Demo.PersonD", index)
    iris_obj.set(index, "^Demo.PersonD")
    elapsed_time = time.process_time() - t
    print("Time took to execute (native): " + str(elapsed_time))

# update entry with name [name] with new [properties]
def update_global(iris_obj: iris.IRIS, properties: list, name: str) -> None:
    t = time.process_time()
    index = iris_obj.get("^Demo.PersonD") + 1
    target = -1
    for i in range(1, index):
        n = iris.IRISList(iris_obj.getBytes("^Demo.PersonD", i)).get(2)
        if n == name: target = i
    if target != -1:
        list = iris.IRISList()
        for property in properties: list.add(property)
        iris_obj.set(list, "^Demo.PersonD", target)
    elapsed_time = time.process_time() - t
    print("Time took to execute (native): " + str(elapsed_time))

# delete the entry with name [name] from the database
def delete_global(iris_obj: iris.IRIS, name: str) -> None:
    t = time.process_time()
    index = iris_obj.get("^Demo.PersonD") + 1
    target = -1
    for i in range(1, index):
        n = iris.IRISList(iris_obj.getBytes("^Demo.PersonD", i)).get(2)
        if n == name: target = i
    if target != -1:
        iris_obj.kill("^Demo.PersonD", target)
        iris_obj.set(index - 2, "^Demo.PersonD")
    elapsed_time = time.process_time() - t
    print("Time took to execute (native): " + str(elapsed_time))

# Execute task based on user input
def execute_selection(selection: int, iris_obj: iris.IRIS) -> None:
    if selection == 1:
        view_globals(iris_obj)
    elif selection == 2:
        name = input("Name: ")
        phone = input("Phone Number: ")
        age = input("Age: ")
        store_global(iris_obj, ["", name, phone, age])
    elif selection == 3:
        old_name = input("Who would you like to update?: ")
        name = input("New Name: ")
        phone = input("New Phone Number: ")
        age = input("New Age: ")
        update_global(iris_obj, ["", name, phone, age], old_name)
    elif selection == 4:
        old_name = input("Who would you like to delete?: ")
        delete_global(iris_obj, old_name)

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

    # Create connection to InterSystems IRIS
    connection = iris.createConnection(ip, port, namespace, username, password)

    print("Connected to InterSystems IRIS")

    # Create an iris object
    iris_native = iris.createIRIS(connection)

    # Populate person global with data
    iris_native.kill("Demo.PersonD")
    iris_native.classMethodValue("Demo.Person", "Populate")

    # Starting interactive prompt
    while True:
        print("1. View data")
        print("2. Store Person data")
        print("3. Update Person data")
        print("4. Delete Person Data")
        print("5. Quit")
        try:
            selection = int(input("What would you like to do? "))
            if selection == 5:
                break
            elif selection not in range(1, 6):
                print("Invalid option. Try again!")
                continue
        except Exception as e:
            print("Error:", e)
        execute_selection(selection, iris_native)

if __name__ == '__main__':
    run()

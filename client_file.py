"""This is a Client module and its functionalities in Client-Server application"""
import asyncio
command_list = []
print("---------------A Python Client-Server Management System Application----------------")
async def client():
    """client is the name of this function and it is used to login or register the user"""
    rdr, wtr = await asyncio.open_connection('127.0.0.1', 8080)
    ip_message = ''
    while True:
        n = input("Enter\n1-Register\n2-Login\n3-Exit:\n")
        try:
            if n == "1":
                input_cmd = (input("Enter the command to register\n - register <username> <password> :"))
                command_list.append(input_cmd)
                input_cmd = input_cmd.split(' ')
                try:
                    if input_cmd[0] != "register":
                        print(" Please check the command - Wrong command")
                    else:
                        path_client = " ".join(str(s) for s in input_cmd)
                        ip_message = path_client
                        wtr.write(ip_message.encode())
                        ip_data = await rdr.read(100)
                        print(f'Received: {ip_data.decode()}')
                    continue
                except IndexError:
                    print("Index Error")
            elif n == "2":
                input_cmd = input("Enter the command to login\n - login <username> <password> :")
                command_list.append(input_cmd)
                input_cmd = input_cmd.split(' ')
                if input_cmd[0] != "login":
                    print(" Please check the command - Wrong command ")
                else:
                    path_client = " ".join(str(s) for s in input_cmd)
                    ip_message = path_client
                    wtr.write(ip_message.encode())
                    ip_data = await rdr.read(100)
                    ip_data = ip_data.decode()
                    print(f'Received: {ip_data}')
                    try:
                        if "User Login succesful" in ip_data:
                            break
                        else:
                            continue
                    except FileNotFoundError:
                        print("Error occurred")
            elif n == "3":
                input_cmd = input("Enter the command to Exit\n - quit:")
                command_list.append(input_cmd)
                input_cmd = input_cmd.split(' ')
                usrr = "user.txt"
                pwd = "1234"
                if input_cmd[0] != "quit":
                    print(" Please check the command - Wrong command ")
                    continue
                elif usrr == pwd:
                    print("Quiting the server!!")
                else:
                    ip_message = input_cmd[0]
                    wtr.write(ip_message.encode())
                    ip_data = await rdr.read(100)
                    print(f'Received: {ip_data.decode()}')
                    quit()
            else:
                ip_data = "Please enter only above options"
                print(f'Received: {ip_data}')
                continue
        except NameError:
            print("Error occurred")

    def commands():
        """This is a commands function which gives the total information regarding all avaliable commands and how to use them."""
        print('''--------------------COMMAND LISTS TO PERFORM OPERATIONS-------------------

    1) change_folder <name>
        --"change_folder" command is used to change the directory to the given folder name. Here <name> defines the folder name\n
    2) list
        --"list" command is used to print the list of all folders and files in the current working directory.\n
    3) read_file <name>
        --"read_file" command is used to read the given file and prints the data on screen. Here <name> defines the file name\n
    4) write_file <name> <input>
        --"write_file" command is used to write(append) the data written as input to the given file name.
           Here <name> defines the name of the file and <input> defines the input data that needed to be added in the file.\n
    5) create_folder <name>
        --"create_folder" command is used to create a folder in current working directory. Here <name> defines the folder name.\n
    6) register <username> <password>
        --"register" command is used to register the new user. Here <username> defines the username of user choice and <password> defines the users choice password.\n
    7) login <username> <password>
        --"login" command is used to login the user into the server. Here <username> defines the username of user and <password> defines the users password.\n
    8) commands
        --"commands" command is used to print all the commands.\n
    9) quit
        --"quit" command is used to log out the user from the server.
--------------------------------------------------------------------------------------''')
    commands()
    while True:
        input_cmd = input("Enter the command:")
        command_list.append(input_cmd)
        input_cmd = input_cmd.split(' ')
        usr="user.txt"
        adm="admin.txt"
        try:
            if len(input_cmd) == 1:
                try:
                    if input_cmd[0] == "commands":
                        commands()
                        continue
                    elif input_cmd[0] == "quit":
                        ip_message = input_cmd[0]
                        wtr.write(ip_message.encode())
                        ip_data = await rdr.read(100)
                        print(f'Received: {ip_data.decode()}')
                        quit()
                    elif input_cmd[0] == "register" or input_cmd[0] == "login":
                        print("User already logged in")
                    else:
                        path_client = " ".join(str(s) for s in input_cmd)
                        ip_message = path_client
                        wtr.write(ip_message.encode())
                        ip_data = await rdr.read(2048)
                        print(f'Received: {ip_data.decode()}')
                        continue
                except NameError:
                    print("Name error occurred")
            else:
                if input_cmd[0] == "register" or input_cmd[0] == "login":
                    print("User already logged in")
                elif input_cmd[0] == "quit":
                    ip_message = input_cmd[0]
                    wtr.write(ip_message.encode())
                    ip_data = await rdr.read(100)
                    print(f'Received: {ip_data.decode()}')
                    quit()
                elif usr == adm:
                    print("Received client side")
                else:
                    path_client = " ".join(str(s) for s in input_cmd)
                    ip_message = path_client
                    wtr.write(ip_message.encode())
                    ip_data = await rdr.read(2048)
                    print(f'Received: {ip_data.decode()}')
                    continue
        except IndexError:
            print("Index Error")
asyncio.run(client())
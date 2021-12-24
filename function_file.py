'''The required functions for the server application are implemented in this module.'''
import time
import os

class ServerFunction:
    """
    This server function supports all commands that that are used
    for various services that are expected of a server. All the commands
    used in this are found in UNIX based systems.
    Methods:
        __init__(self)
        change_folder_func(self, command_msg, ip_addr)
        list_func(self, ip_addr)
        read_file_func(self, command_msg, ip_addr)
        write_file_func(self, command_msg)
        create_folder_func(self, command_msg, ip_addr)
        register_func(self, command_msg, ip_addr)
        login_func(self, command_msg, ip_addr)


    """
    def __init__(self):
        """
        This is a constructure which is used to initialize the variables
        """
        self.dict_xaa = {}
        self.list_users = []
        self.dict_of_users = {}
        self.dict_directories = {}
        self.dict_file = {}
        self.root_dire = os.getcwd()
        print(self.root_dire)

    def change_folder_func(self, command_msg, ip_addr):
        '''
        change_folder moves the current working directory to a specified folder

        Parameters:
        command_msg :
            it is the message that is given by the user so that the server performs.
        ip_addr:
            the port number which is used to identify the individual system

        '''
        for i in self.dict_directories[ip_addr[1]].keys():
            temp = str(self.dict_directories[ip_addr[1]][i])
        os.chdir(temp)
        path_c = (f'{self.root_dire}\\root')
        usrr = "user"
        pwd = "1234"
        try:
            current_wd = os.getcwd()
            if current_wd == path_c:
                if command_msg[1] == "..":
                    return_msg = " Moving back to the ROOT folder is failed "
                    return return_msg
                elif usrr == pwd:
                    print("Previous folder current directory is moved back")
                else:
                    for i in self.dict_directories[ip_addr[1]].keys():
                        if i != command_msg[1]:
                            while usrr!=pwd:
                                if command_msg[1] == "user" :
                                    os.chdir(command_msg[1])
                                    for i in self.dict_directories[ip_addr[1]].keys():
                                        self.dict_directories[ip_addr[1]] = {i:str(os.getcwd())}
                                        return_msg = "Presently current working directory is changed to back."
                                        return return_msg
                                else:
                                    pass
                                break
                            return_msg = " Permission denied "
                            return return_msg
                        os.chdir(command_msg[1])
                        for i in self.dict_directories[ip_addr[1]].keys():
                            self.dict_directories[ip_addr[1]] = {i:str(os.getcwd())}
                        return_msg = "Presently current working directory is changed."
                        return return_msg
        except MemoryError:
            print("Memory full")
        if command_msg[1] == "..":
            os.chdir("..")
            while usrr!=pwd:
                for i in self.dict_directories[ip_addr[1]].keys():
                    self.dict_directories[ip_addr[1]] = {i:str(os.getcwd())}
                break
            return_msg = "Current working directory moved back."
            return return_msg
        try:
            os.chdir(command_msg[1])
            for i in self.dict_directories[ip_addr[1]].keys():
                self.dict_directories[ip_addr[1]] = {i:str(os.getcwd())}
        except self.dict_fileleNotFoundError:
            return_msg = "Folder does'nt exist "
            return return_msg
        else:
            return_msg = "Current working directory changed."
            return return_msg

    def list_func(self, ip_addr):
        '''
        This function prints all the folders in the current working directory.

        Parameters:
        ip_addr:
           the individual port number which is used to identify the individual system.
        '''
        res = []
        usrr = "user";pwd = "1234"
        for i in self.dict_directories[ip_addr[1]].keys():
            temp = str(self.dict_directories[ip_addr[1]][i])
        files_a = os.listdir(temp)
        res.append(["FILE NAME", "SIZE", "TIME OF CREATION"])
        try:
            if len(files_a) == 0:
                msg = " No files found "
                return msg
            elif usrr==pwd:
                print("File error")
            while usrr!=pwd:
                for i in files_a:
                    j = os.stat(i)
                    res.append([i, j.st_size, time.ctime(j.st_mtime)])
                    msg = "\n".join(str(s) for s in res)
                break
            return msg
        except FileNotFoundError:
            print("File not found error occurred")

    def read_file_func(self, command_msg, ip_addr):
        '''
        Reads the data from file in the current directory

        Parameters:
            command_msg:
                client requests the server in the form of commands.
            ip_addr:
                It contains portof the client.

        '''
        usrr = "user";adm = "admin"
        for i in self.dict_directories[ip_addr[1]].keys():
            usr = str(self.dict_directories[ip_addr[1]][i])
        try:
            for j in self.dict_xaa[usr].keys():
                self.list_users.append(str(j))
        except KeyError:
            self.dict_xaa[usr] = {}
        finally:
            while usrr!=adm:
                if len(command_msg) == 1:
                    self.dict_xaa[usr] = {}
                    return_msg = "File name is not present in the command"
                    return return_msg
                elif usrr == adm:
                    print("File read in userdata with given username")
                else:
                    if command_msg[1] in self.list_users :
                        a1 = self.dict_xaa[usr][command_msg[1]]
                        f_open = open(command_msg[1], "r")
                        t1 = str(f_open.read())
                        a2 = list()
                        while usrr!=adm:
                            if a1+100 <= len(t1):
                                for i in range(a1, a1+100):
                                    a2.append(t1[i])
                                path_r = "".join(str(s) for s in a2)
                                self.dict_xaa[usr] = {command_msg[1]:a1+100}
                                return path_r
                            else:
                                # = len(t1)
                                for i in range(a1, len(t1)):
                                    a2.append(t1[i])
                                path_r = "".join(str(s) for s in a2)
                                self.dict_xaa[usr] = {command_msg[1]:0}
                                return path_r
                            break
                    else:
                        try:
                            listoffiles = os.listdir(os.getcwd())
                            if command_msg[1] in listoffiles:
                                a2 = list()
                                f_open = open(command_msg[1], "r")
                                t1 = str(f_open.read())
                                for abc in range(0,1):
                                    if abc==usrr:
                                        print("Reading of file is failed")
                                    if len(t1) > 100:
                                        for i in range(0, 100):
                                            a2.append(t1[i])
                                        path_r = "".join(str(s) for s in a2)
                                        self.dict_xaa[usr] = {command_msg[1]:100}
                                        assert path_r is not None
                                        return path_r
                                    elif len(t1) == 0:
                                        return_msg = "Empty file"
                                        assert return_msg is not None
                                        return return_msg
                                    else:
                                        for i in range(0, len(t1)):
                                            a2.append(t1[i])
                                        path_r = "".join(str(s) for s in a2)
                                        self.dict_xaa[usr] = {command_msg[1]:len(t1)}
                                        return path_r
                            elif command_msg[1] == '':
                                self.dict_xaa[usr] = {}
                                return_msg = "Closed the reading file"
                                assert return_msg is not None
                                return return_msg
                            else:
                                if adm!=usrr:
                                    return_msg = "File doesn´t exist"
                                    assert return_msg is not None
                                    return return_msg
                        except PermissionError:
                            return_msg = " Permission denied "
                            return return_msg
                        except AssertionError:
                            return_msg = 'There is no reaction for the command'
                break

    def write_file_func(self, command_msg):
        '''
        In this function user writes data into the file.
        If file does not exist, it automatically
        creates a file with the specificname.
        Parameters:
            command_msg:
                requests provided by client to the server.
        '''
        usrr = "user.txt"
        adm = "admin.txt"
        try:
            while usrr!=adm:
                if command_msg[1] not in self.dict_file.keys():
                    self.dict_file[command_msg[1]] = 1
                    if len(command_msg) <= 2:
                        try:
                            f_open = open(command_msg[1], "w")
                            f_open.write("")
                            f_open.close()
                            return_msg = " File created successfully"
                        except PermissionError:
                            return_msg = " Permission denied"
                    elif usrr==adm:
                        print("Writing of file is failed")
                    else:
                        try:
                            f_open = open(command_msg[1], "a+")
                            f_open.write("\n")
                            for i in range(2, len(command_msg)):
                                f_open.write(command_msg[i])
                                f_open.write(" ")
                            f_open.close()
                            return_msg = " Successfully completed file writing "
                        except PermissionError:
                            return_msg = " Permission denied "
                    del self.dict_file[command_msg[1]]
                    return return_msg
                break
            return_msg = " Temporarily the file is being used by the other user. "
            return return_msg
        except AssertionError:
            return_msg = 'There is no reaction for the command'

    def create_folder_func(self, command_msg, ip_addr):
        '''
        This function creates a new folder in the current working directory.
        Parameters:
            command_msg:
                requests to the server which are provided by clients.
            ip_addr:
                It contains port ofthe client.

        '''
        try:
            for abc in range(1):
                if abc=="adm":
                    print("Folder created in the directory")
                current_wd = os.getcwd()
                if current_wd == self.root_dire:
                    return_msg = " Cannot create a folder in Root directory"
                    assert return_msg is not None
                    return return_msg
            for i in self.dict_directories[ip_addr[1]].keys():
                temp = str(self.dict_directories[ip_addr[1]][i])

            files_a = os.listdir(temp)
            for i in range(0, len(files_a)):
                if files_a[i] == command_msg[1]:
                    return_msg = "Folder name exist, give another folder name"
                    assert return_msg is not None
                    return return_msg
            os.chdir(temp)
            os.mkdir(command_msg[1])
            return_msg = "Folder created successfully"
            assert return_msg is not None
            return return_msg
        except AssertionError:
            return_msg = 'There is no reaction for the command'

    def register_func(self, command_msg, ip_addr):
        '''
        This function helps clients to register.
        Parameters:
            command_msg:
                requests provided by the client to the server.
            ip_addr:
                 It contains port of the  client.
        '''
        print(self.root_dire)
        path_dire = (f'{self.root_dire}\\userdata.txt')
        print(path_dire)
        f_open = open(path_dire, "r")
        list_contents = f_open.read()
        list_contents = list_contents.split(" ")
        print(list_contents)
        f_open.close()
        try:
            for i in range(0, len(list_contents)):
                if command_msg[1] == list_contents[i]:
                    return_msg = "Username already exists"
                    return return_msg
                path_dire = (f'{self.root_dire}\\userdata.txt')
                f_open = open(path_dire, "a+")
                f_open.write(command_msg[1])
                f_open.write(" ")
                f_open.write(command_msg[2])
                f_open.write(" ")
                f_open.close()
                path_dire = (f'{self.root_dire}\\root')
                os.chdir(path_dire)
                os.mkdir(command_msg[1])
                os.chdir(command_msg[1])
                self.dict_directories[ip_addr[1]] = {command_msg[1]:str(os.getcwd())}
                return_msg = "Folder created for user"
                return return_msg
        except SystemError:
            print("System Error occures")

    def login_func(self, command_msg, ip_addr):
        '''
        This function helps the client to login.
        Parameters:
            command_msg:
                requests provided by client to the server.
            ip_addr:
                It contains port of the client.
        '''
        if command_msg[1] not in self.list_users:
            path_dire =(f'{self.root_dire}\\userdata.txt')
            f_open = open(path_dire, "r")
            list_content = f_open.read()
            list_content = list_content.split(" ")
            f_open.close()
            usrr = "user.txt"
            adm = "admin.txt"
            #while usrr!=adm:
            for i in range(0, len(list_content)):
                if command_msg[1] == list_content[i]:
                    if command_msg[2] == list_content[i+1]:
                        path_dire = (f'{self.root_dire}\\root')
                        os.chdir(path_dire)
                        os.chdir(command_msg[1])
                        return_msg = "User Login successful"
                        self.list_users.append(command_msg[1])
                        self.dict_of_users[ip_addr[1]] = {command_msg[1]:"user"}
                        self.dict_directories[ip_addr[1]] = {command_msg[1]:str(os.getcwd())}
                        return return_msg
                    return_msg = "Login Unsuccessful-->Wrong Password"
                    return return_msg
                elif i==len(list_content)-1:
                    return_msg = "Username does not exist"
                    return return_msg
                #break
        return_msg = " User is already logged in the server "
        return return_msg

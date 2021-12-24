''' This module contains the implementation of the server'''
import signal
import asyncio
from function_file import *
signal.signal(signal.SIGINT, signal.SIG_DFL)
async def operations(reader, writer):
    '''
    Establishes a connection between client and server.
    Operations such as read and write are performed.
    The given commands are preprocessed and respective functions are called.
    parameters:
    ---------------
    reader:
        Performs the read operation .
    writer:
        Performs the write operation.
    '''
    obj = ServerFunction()

    ip_address = writer.get_extra_info('peername')
    input_message = f"Connected to {ip_address}"
    while 1:
        try:
            info = await reader.read(100)
            print(info)
            input_message = info.decode().strip()
            print(f"Received {input_message} from {ip_address}")
            input_message = input_message.split(' ')
            if 'register' in input_message:
                input_message = obj.register_func(input_message, ip_address)
            elif "login" in input_message:
                input_message = obj.login_func(input_message, ip_address)
            elif "list" in input_message:
                input_message = obj.list_func(ip_address)
            elif "create_folder" in input_message:
                input_message = obj.create_folder_func(input_message, ip_address)
            elif "write_file" in input_message:
                input_message = obj.write_file_func(input_message)
            elif "change_folder" in input_message:
                input_message = obj.change_folder_func(input_message, ip_address)
            elif "read_file" in input_message:
                input_message = obj.read_file_func(input_message, ip_address)
            elif "quit" in input_message:
                input_message = "Connection is closed"
                try:
                    del obj.dict_of_users[ip_address[1]]
                    del obj.dict_directories[ip_address[1]]
                    del obj.dict_xaa[ip_address[1]]
                except KeyError:
                    pass
                finally:
                    path_m = "".join(str(s) for s in input_message)
                    print(f"Send: {path_m}")
                    writer.write(path_m.encode())
                    break
            else:
                input_message = "Wrong Command"
            path_m = "".join(str(s) for s in input_message)
            print(f"Sent: {path_m}")
            writer.write(path_m.encode())
        except ValueError:
            print("Value error occurred")

async def main():
    ''' Here the server starts its execution.'''
    server = await asyncio.start_server(operations, '127.0.0.1', 8080)
    ip_address = server.sockets[0].getsockname()
    print(f'Serving on {ip_address}')
    async with server:
        await server.serve_forever()
asyncio.run(main())
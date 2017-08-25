# client file

import socket

# create socket object
s = socket.socket()
# get local machine address
host = socket.gethostname()
# reserve a port for a service
port = 6000

s.connect((host, port))
s.send(b'hello server!')

with open('received_file', 'wb') as f:
    print('file opened')

    while 1:
        print('...receiving data...')
        data = s.recv(1024)
        print(data)

        if not data:
            break

        # write data to a file
        f.write(data)

f.close()
print('successfully got the file')
s.close()
print('connection closed')

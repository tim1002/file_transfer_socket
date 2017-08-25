# server file

import socket

# create socket object
s = socket.socket()
# get local machine address
host = socket.gethostname()
# reserve a port for a service
port = 6000
# bind created socket to the port
s.bind((host, port))
# wait for client connection
s.listen(5)

print('...server listening...')

while 1:
    # establish connection with client
    conn, addr = s.accept()

    print('got connection from', addr)
    data = conn.recv(1024)
    print('server received', repr(data))

    filename = 'mytext.txt'
    f = open(filename, 'rb')
    l = f.read(1024)

    while (l):
        conn.send(l)
        print('sent ', repr(l))
        l = f.read(1024)

    f.close()

    print('done sending')
    conn.send(b'thank you for connecting')
    conn.close()

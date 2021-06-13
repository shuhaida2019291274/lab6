import socket
import signal
import sys

c = socket.socket()
host = '192.168.56.103'
port = 8888

print('Waiting for connection...')
try:
    c.connect((host, port))
except socket.error as e:
    print(str(e))

Response = c.recv(1024)
print(Response.decode("utf-8"))
while True:
    print("Choose any mathematical function below :")
    print("Logarithmic(l)")
    print("Square Root(s)")
    print("Exponential(e)")
    Input = input('\nEnter function code in the () : ')

    if Input == 'l' or Input == 's' or Input == 'e':
        n = input("Enter any number: ")
        Input = Input + ":" + n
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

    elif Input == 'exit':
        break

    else:
        print("You have entered wrong input. Please try again...")
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

c.close()

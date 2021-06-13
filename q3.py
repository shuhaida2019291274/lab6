import math
import socket
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode('\nAIDIOUS CALCULATOR'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        try:
            operation, val = data.split(":")
            opt = str(operation)
            n = float(val)

            if opt[0] == 'l':
                opt = 'Logarithmic'
                ans = math.log10(n)
            elif opt[0] == 's':
                opt = 'Square Root'
                ans = math.sqrt(n)
            elif opt[0] == 'e':
                opt = 'Exponential'
                ans = math.exp(n)
            else:
                answer = ('error...')

            sendAns = (str(opt)+ '['+ str(n) + ']= ' + str(ans))
            print ('\nCalculation is done!!!')
        except:
            print ('Connection with client terminated...')
            sendAns = ('Connection with client terminated...')

        if not data:
            break

        s_sock.send(str.encode(str(sendAns)))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("Server is listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                print("Connected to the client...")
                p.start()

            except socket.error:

                print('Socket error')

    except Exception as e:
                print("An exception occurred!")
                print(e)
                sys.exit(1)
    finally:
     	   s.close()

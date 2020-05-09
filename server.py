import socket
import math

serverName = 'Localhost'
serverPort = 12456
bufferSize = 2048
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('localhost', 12456))
print('The server is connected.')

while 1:
    print('Listening...')

    operator, clientAddress = serverSocket.recvfrom(bufferSize)
    print('Operator received: ', operator)

    if operator == b'+' or operator == b'-' or operator == b'/' or operator == b'*':

        operand1, clientAddress = serverSocket.recvfrom(bufferSize)
        print('Operand 1 received:', operand1)

        operand2, clientAddress = serverSocket.recvfrom(bufferSize)
        print('Operand 2 received:', operand2)

        print('Calculating...')
        break

    elif operator == b'sin' or operator == b'cos' or operator == b'tan' or operator == b'cot':
        operand1, clientAddress = serverSocket.recvfrom(bufferSize)
        print('Operand received:', operand1)

        print('Calculating...')
        break

if operator == b'+':
    answer = float(operand1.decode()) + \
        float(operand2.decode())
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'-':
    answer = float(operand1.decode()) - float(operand2.decode())
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'/':
    answer = float(operand1.decode()) / float(operand2.decode())
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'*':
    answer = float(operand1.decode()) * float(operand2.decode())
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'sin':
    answer = math.sin(float(operand1.decode()))
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'cos':
    answer = math.cos(float(operand1.decode()))
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'tan':
    answer = math.sin(float(operand1.decode()))
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'cot':
    answer = math.sin(float(operand1.decode()))
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)

print('Calculation finished.')
serverSocket.close()
print('Socket closed.')

import socket
import math
import timeit

serverName = 'Localhost'
serverPort = 12456
bufferSize = 2048
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('localhost', 12456))
print('The server is connected.')

while True:
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
    start = timeit.timeit()
    answer = float(operand1.decode()) + \
        float(operand2.decode())
    end = timeit.timeit()
    timeElapsed = end - start
    timeElapsed = str(timeElapsed)

    print(timeElapsed)

    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
    serverSocket.sendto(timeElapsed.encode(), clientAddress)
elif operator == b'-':
    start = timeit.timeit()
    answer = float(operand1.decode()) - float(operand2.decode())
    end = timeit.timeit()
    timeElapsed = end - start
    timeElapsed = str(timeElapsed)

    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
    serverSocket.sendto(timeElapsed.encode(), clientAddress)
elif operator == b'/':
    start = timeit.timeit()
    answer = float(operand1.decode()) / float(operand2.decode())
    end = timeit.timeit()
    timeElapsed = end - start
    timeElapsed = str(timeElapsed)

    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
    serverSocket.sendto(timeElapsed.encode(), clientAddress)
elif operator == b'*':
    start = timeit.timeit()
    answer = float(operand1.decode()) * float(operand2.decode())
    end = timeit.timeit()
    timeElapsed = end - start
    timeElapsed = str(timeElapsed)

    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
    serverSocket.sendto(timeElapsed.encode(), clientAddress)
elif operator == b'sin':
    start = timeit.timeit()
    answer = math.sin(float(operand1.decode()))
    end = timeit.timeit()
    timeElapsed = end - start
    timeElapsed = str(timeElapsed)

    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
    serverSocket.sendto(timeElapsed.encode(), clientAddress)
elif operator == b'cos':
    start = timeit.timeit()
    answer = math.cos(float(operand1.decode()))
    end = timeit.timeit()
    timeElapsed = end - start
    timeElapsed = str(timeElapsed)

    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
    serverSocket.sendto(timeElapsed.encode(), clientAddress)
elif operator == b'tan':
    start = timeit.timeit()
    answer = math.sin(float(operand1.decode()))
    end = timeit.timeit()
    timeElapsed = end - start
    timeElapsed = str(timeElapsed)

    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
    serverSocket.sendto(timeElapsed.encode(), clientAddress)
elif operator == b'cot':
    start = timeit.timeit()
    answer = math.sin(float(operand1.decode()))
    end = timeit.timeit()
    timeElapsed = end - start
    timeElapsed = str(timeElapsed)

    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
    serverSocket.sendto(timeElapsed.encode(), clientAddress)

print('Calculation finished.')
serverSocket.close()
print('Socket closed.')

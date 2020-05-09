import socket

serverName = 'Localhost'
serverPort = 12456
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('localhost', 12456))
print('The server is connected')
while 1:

    print('Listening...')
    number1, clientAddress = serverSocket.recvfrom(2048)
    print('Number1 received:', number1)

    number2, clientAddress = serverSocket.recvfrom(2048)
    print('Number2 received:', number2)

    operator, clientAddress = serverSocket.recvfrom(2048)
    print('Received operator: ', operator)
    print('Calculating...')
    break

if operator == b'+':
    print('Started operation: ', operator)
    answer = int(number1.decode()) + \
        int(number2.decode())
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'-':
    print('Started operation: ', operator)
    answer = int(number1.decode()) - int(number2.decode())
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'/':
    print('Started operation: ', operator)
    answer = int(number1.decode()) / int(number2.decode())
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)
elif operator == b'*':
    print('Started operation: ', operator)
    answer = int(number1.decode()) * int(number2.decode())
    answer = str(answer)
    serverSocket.sendto(answer.encode(), clientAddress)

print('Calculation finished.')
serverSocket.close()
print('Socket closed.')

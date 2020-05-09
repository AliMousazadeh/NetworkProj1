import socket

serverName = 'Localhost'
serverport = 12456
bufferSize = 2048
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Traget IP: ', serverName)
print('Target Port:', serverport)
print('\n')

while True:

    operator = input(
        'Select an operator (+ - / * sin cos tan cot EOC (End Of Connection)): ')

    if operator == '+' or operator == '-' or operator == '/' or operator == '*':
        operand1 = input('Input operand 1: ')
        operand2 = input('Input operand 2: ')

        clientSocket.sendto(operator.encode(), (serverName, serverport))
        clientSocket.sendto(operand1.encode(), (serverName, serverport))
        clientSocket.sendto(operand2.encode(), (serverName, serverport))

    elif operator == 'sin' or operator == 'cos' or operator == 'tan' or operator == 'cot':
        operand1 = input('Input operand: ')

        clientSocket.sendto(operator.encode(), (serverName, serverport))
        clientSocket.sendto(operand1.encode(), (serverName, serverport))

    elif operator == 'EOC':
        clientSocket.sendto(operator.encode(), (serverName, serverport))
        print('Connection terminated.')
        break
    else:
        print('Invalid operator.')

    answer, serverAddress = clientSocket.recvfrom(bufferSize)
    timeElapsed, serverAddress = clientSocket.recvfrom(bufferSize)
    print('Result: ', answer)
    print('Time elapsed: ', timeElapsed)

clientSocket.close()

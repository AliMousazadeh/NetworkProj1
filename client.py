import socket

serverName = 'Localhost'
serverport = 12456
bufferSize = 2048
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Traget IP: ', serverName)
print('Target Port:', serverport)
print('\n')

operator = input('Select an operator (+ - / * sin cos tan cot): ')

if operator == '+' or operator == '-' or operator == '/' or operator == '*':
    operand1 = input('Input operand 1: ')
    operand2 = input('Input operand 2: ')

    clientSocket.sendto(operator.encode(), (serverName, serverport))
    clientSocket.sendto(operand1.encode(), (serverName, serverport))
    clientSocket.sendto(operand2.encode(), (serverName, serverport))
else:
    operand1 = input('Input operand: ')

    clientSocket.sendto(operator.encode(), (serverName, serverport))
    clientSocket.sendto(operand1.encode(), (serverName, serverport))

answer, serverAddress = clientSocket.recvfrom(bufferSize)
print('Result: ', answer)

clientSocket.close()

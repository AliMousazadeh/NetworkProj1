import socket

serverName = 'Localhost'
serverport = 12456
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Traget IP: ', serverName)
print('Target Port:', serverport)
print('\n')


number1 = input('Input number1: ')
number2 = input('Input number2: ')
operator = input('Select an operator: (+ / * -) ')

clientSocket.sendto(number1.encode(), (serverName, serverport))
clientSocket.sendto(number2.encode(), (serverName, serverport))
clientSocket.sendto(operator.encode(), (serverName, serverport))

answer, serverAddress = clientSocket.recvfrom(2048)
print('your result: ', answer)

clientSocket.close()

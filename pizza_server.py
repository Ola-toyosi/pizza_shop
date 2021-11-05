import socket
import sqlite3
import json

conn = sqlite3.connect("pizza.db")
cursor = conn.cursor()

toppings = []
prices = {}

for i in cursor.execute('select * from Toppings'):
    toppings.append(i[0])

for x in cursor.execute('select * from Prices'):
    prices[x[0]] = x[1]

cursor.close()
conn.close()

print(prices['Medium'])

packaged_toppings = str.encode(json.dumps(toppings))
packaged_prices = str.encode(json.dumps(prices))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5421
server.bind((host, port))
server.listen()


while True:

    print(f'server started, running on port{port}')
    client, addr = server.accept()
    client.send(str.encode(f'Accepted connection from {addr}'))
    # client.send(str.encode(f'connection successful! {addr}'))

    while True:
        request = bytes.decode(client.recv(1024)).lower()
        if request == 'p':
            client.send(packaged_prices)
        elif request == 't':
            client.send(packaged_toppings)
        elif request == 'q':
            print(f'disconnecting from {addr}')
            break
        else:
            print('invalid request')
            print(f'disconnecting from {addr}')
            break

    if input('enter q to stop').upper() == 'Q':
        break


# print(toppings)
# print(prices)

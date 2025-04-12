import socket

HOST = 'localhost'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    server1 = 0
    client1 = 0
    while server1 < 3 and client1 < 3:
        # Wysłanie wyboru do serwera
        choice = input('Twoj wybor: ').lower()
        s.sendall(choice.encode('utf-8'))

        # Odbiór wyboru serwera
        server_choice = s.recv(1024).decode("utf-8")
        print(f"Serwer wybrał: {server_choice}")

        # Odbiór wyników (server, client)
        response = s.recv(1024).decode("utf-8")
        server1, client1 = map(int, response.split(","))

        print(f"Aktualny wynik (server:client) to: {server1}:{client1}")

print("Koniec gry!")

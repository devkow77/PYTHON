import socket

HOST = 'localhost'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        # wyniki graczy
        client = 0
        server = 0
        # wyswietlenie polaczenia z serwerem
        print('Connected by', addr)
        while (client < 3 and server < 3):
            # wyslanie wyboru do klienta
            choice = input('Twoj wybor: ').lower()
            conn.sendall(choice.encode('utf-8'))
            # otrzymanie odpowiedzi z klienta
            res = conn.recv(1024).decode("utf-8")
            print('Odpowiedz z klienta: ', res)
            if choice == res:
                print("Remis!")
            if((choice == 'kamien' and res == 'nozyczki') or (choice == 'papier' and res == 'kamien') or (choice == 'nozyczki' and res == 'papier')):
                print('Server zdobywa punkt!')
                server += 1
            else:
                print('Client zdobywa punkt!')
                client += 1
            conn.sendall(f"{server},{client}".encode("utf-8"))
            print(f'Aktualny wynik rozgrywki (server:client) to {server}:{client}')
        print("Koniec gry!")
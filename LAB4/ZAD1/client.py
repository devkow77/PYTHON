import socket

HOST = 'localhost'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # wyslanie wiadomosci do serwera
    msg = "time"
    s.sendall(msg.encode("utf-8"))
    # odebranie odpowiedzi z serwera
    res = s.recv(1024).decode("utf-8")
    print(f"Odpowiedz z serwera: {res}")

import socket
import threading
from pydoc import browse

HOST = "localhost"
PORT = 50007

clients = {}

def handle_client(conn, addr):
    # obsluga pojedynczego klienta
    try:
        conn.sendall("Podaj swoj nick: ".encode("utf-8"))
        nick = conn.recv(1024).decode('utf-8').strip()

        if not nick or nick in clients:
            conn.sendall("Nick jest pusty lub juz zajety!".encode("utf-8"))
            conn.close()
            return

        clients[nick] = conn
        broadcast(f"{nick} dolaczyl do czatu!", sender=nick)
        conn.sendall("Witaj na czacie! \n".encode("utf-8"))

        while True:
            msg = str(conn.recv(1024).decode("utf-8"))
            if not msg:
                break
            if msg.startswith("/"): # Komendy
                if msg.startswith("/kick") and addr[0] == "127.0.0.1":
                    _, target_nick = msg.split(maxsplit=1)
                    if target_nick in clients:
                        clients[target_nick].sendall("Zostales wyrzucony z czatu!".encode("utf-8"))
                        remove_client(target_nick)
                        conn.sendall(f"{target_nick} zostal wyrzucony!".encode("utf-8"))
                    else:
                        conn.sendall(f"Nie znaleziono uzytkownika {target_nick}".encode("utf-8"))
                else:
                    conn.sendall(f"Nieznana komenda!".encode("utf-8"))
            else:
                broadcast(f"{nick}: {msg}", sender=nick)



def start_server():
    # uruchomienie servera
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server is listening at: {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()

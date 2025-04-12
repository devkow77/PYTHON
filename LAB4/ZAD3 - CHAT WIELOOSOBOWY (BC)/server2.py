import socket
import threading

HOST = 'localhost'
PORT = 50007

clients = {}  # Przechowuje klientów w formacie {nick: conn}


def broadcast(message, sender=None):
    """Wysyła wiadomość do wszystkich klientów (oprócz nadawcy, jeśli podany)."""
    for nick, conn in clients.items():
        if nick != sender:
            try:
                conn.sendall(message.encode('utf-8'))
            except:
                remove_client(nick)


def remove_client(nick):
    """Usuwa klienta z listy i powiadamia innych."""
    if nick in clients:
        del clients[nick]
        broadcast(f"🔴 {nick} opuścił czat.")


def handle_client(conn, addr):
    """Obsługuje pojedynczego klienta."""
    try:
        conn.sendall("Podaj swój nick: ".encode('utf-8'))
        nick = conn.recv(1024).decode('utf-8').strip()

        if not nick or nick in clients:
            conn.sendall("⚠️ Nick jest pusty lub już zajęty!".encode('utf-8'))
            conn.close()
            return

        clients[nick] = conn
        broadcast(f"🟢 {nick} dołączył do czatu!", sender=nick)
        conn.sendall("✅ Witaj na czacie!\n".encode('utf-8'))

        while True:
            msg = conn.recv(1024).decode('utf-8')
            if not msg:
                break

            if msg.startswith("/"):  # Komendy
                if msg.startswith("/kick") and addr[0] == '127.0.0.1':
                    _, target_nick = msg.split(maxsplit=1)
                    if target_nick in clients:
                        clients[target_nick].sendall("❌ Zostałeś wyrzucony z czatu.".encode('utf-8'))
                        remove_client(target_nick)
                        conn.sendall(f"✅ {target_nick} został wyrzucony.".encode('utf-8'))
                    else:
                        conn.sendall(f"⚠️ Nie znaleziono użytkownika {target_nick}.".encode('utf-8'))
                else:
                    conn.sendall("⚠️ Nieznana komenda!".encode('utf-8'))
            else:
                broadcast(f"{nick}: {msg}", sender=nick)

    except:
        pass
    finally:
        remove_client(nick)
        conn.close()


def start_server():
    """Uruchamia serwer."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"🖥 Serwer uruchomiony na {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()


if __name__ == "__main__":
    start_server()

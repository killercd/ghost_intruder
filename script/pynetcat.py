import socket
import sys
import signal
from colorama import init, Fore, Style


def signal_handler(sig, frame):
    print('Exiting...')
    sys.exit(0)



def server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[*] Listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"[+] Connection from {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(Fore.GREEN+f"CLIENT> {data.decode()}", end="")
                sdata = input(Fore.RED+"SERVER> ")
                conn.sendall(sdata.encode('utf-8'))

def main():
    print("Pynetcat server")
    listen_iface = input("Listen interface (default: 0.0.0.0): ") or "0.0.0.0"
    listen_port = input("Listen port (default: 9090): ")
    listen_port = 9090 if not listen_port else int(listen_port)
    server(listen_iface, listen_port)

if __name__=="__main__":
    signal.signal(signal.SIGINT, signal_handler)
    init(autoreset=True)
    main()
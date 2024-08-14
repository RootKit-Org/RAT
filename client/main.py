# Python Program to Get IP Address
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

logging.info("Your Computer Name is: %s", hostname)
logging.info("Your Computer IP Address is: %s", IPAddr)

logging.info("hello client")

while True:
    pass
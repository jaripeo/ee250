"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('172.20.10.4', 6767))

    while True:
        # TODO: Get user input and send it to the server using your TCP socket
        message = input("Enter a message to send (or type 'quit' to exit): ")

        if message == "quit":
            break
            
        client_socket.sendall(message.encode())

        # TODO: Receive a response from the server and close the TCP connection
        response = client_socket.recv(1024).decode()
        print("Server response: ", response)

    client_socket.close() 



if __name__ == '__main__':
    main()
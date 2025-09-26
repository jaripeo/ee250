# Lab 2

## Team Members
- Dave Rodriguez

## Lab Question Answers

Answer for Question 1: 

The reliability of UDP significantly decreased when 50% packet loss was introduced. Since UDP is connectionless and does not implement retransmission or acknowledgment mechanisms, any lost packets are simply dropped without recovery. This occurred because UDP relies on the underlying network to deliver packets, and with a 50% loss rate, half of the messages were never received by the destination.

Q2:

TCP maintained high reliability despite the 50% packet loss, but at the cost of increased latency. This is because TCP uses acknowledgments, retransmissions, and congestion control to ensure that all data is delivered correctly. When packets were dropped, TCP detected the loss and resent the missing segments, preserving data integrity.


Q3:

The speed of TCP responses decreased due to the increased number of retransmissions and the activation of congestion control algorithms. TCP interprets packet loss as a sign of network congestion, which causes it to reduce its transmission rate (e.g., via slow start or congestion avoidance). This throttling, combined with the time spent waiting for acknowledgments and resending lost packets, led to slower overall throughput.


TCP_SERVER.C Questions

Q1:

argc is the number of command-line arguments passed to the program (including the program name itself)
argv[] is an array of strings (character pointers) representing each argument. For example, running ./server 8080, then argc is 2, argv[0] is "./server" and argv[1] is "8080"

Q2:

A file descriptor is a non-negative integer that uniquely identififes an open file (or socket) in a process.
The file descriptor table is a per-process table maintained by the operating system that maps file descriptors to open files/resources.

Q3:

A struct in C is a user-defined data type that groups related variables under one name.
struct sockaddr_in is a structure used to specify an endpoint address for IPv4 sockets. It contains fields for the address family, port number, and IP address.

Q4:

Input Parameters:
- socket(int domain, int type, int protocol)
    - domain: Address family (e.g., AF_INET for IPv4)
    - type: Socket type (e.g., SOCK_STREAM for TCP)
    - protocol: Protocol (usually 0 for default)
    - Returns: A file descriptor for the new socket, or -1 on error.

Q5:

- bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
    - sockfd: Socket file descriptor
    - addr: Pointer to address structure (e.g., sockaddr_in)
    - addrlen: Size of the address structure
- listen(int sockfd, int backlog)
    - sockfd: Socket file descriptor
    - backlog: Maximum length of the pending connections queue

Q6:

while(1) is used to keep the server running and accepting new client connections indefinitely.
Problem: The code handles only one client at a time. If multiple clients connect simultaneously, new connections must wait until the current one is finished, causing delays or dropped connections.

Q7:

fork() creates a new child process that is a copy of the parent.
In a server, after accept(), you can call fork(). The child process handles the client, while the parent goes back to accept new connections. This allows the server to handle multiple clients concurrently.

Q8:

A system call is a request from a user-space program to the operating system kernel to perform a privileged operation (like file I/O, creating sockets, etc.). Functions like bind, listen, accept, read, and write are system calls.
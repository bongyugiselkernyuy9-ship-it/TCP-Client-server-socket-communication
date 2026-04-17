# CYBE 6223 — Lab 0 Report

**Group Identification (NAME):**
**Group Members (Names):**
**Date of Submission:**
**GitHub Repository URL:**

---

## 1. Implementation Summary
In this lab, I implemented a basic TCP client-server system using Python sockets.  
The server listens on a specific IP address and port, receives messages from a client, and sends the same message back (echo).  
The client connects to the server, sends a message, receives the response, and prints it to the screen.

## 2. Socket Primitives — What Each Step Does
<!-- For each of the following primitives used in your code, explain
     in one sentence what it does and why it is called at that point:
     socket(), bind(), listen(), accept(), connect(), send/sendall(), recv(), close() -->

| Primitive | Purpose in your code |
|-----------|----------------------|
| socket()  |Creates a communication endpoint for sending and receiving data over the network|
| bind()    | Attaches the server to a specific IP address and port so clients can find it   |
| listen()  | Makes the server wait for incoming client connections                          |
| accept()  | Accepts a client connection and creates a new socket for communication         |
| connect() | Connects the client to the server’s IP and port                                |
| sendall() | Sends data from client to server or server to client reliably                  |
| recv()    | Receives the data sent over the network                                        |
| close()   | Closes the network and free system resources                                   |

## 3. Failure Analysis
<!-- What happens if the client runs before the server is ready?
     What error do you observe? What does this tell you about
     assumptions in distributed systems? (~100 words) -->
If the client runs before the server is ready, a connection error occurs, typically a ConnectionRefusedError. This happens because the client attempts to connect to a port where no server is listening.

This shows that distributed systems depend on timing and availability of services. The client assumes the server is already running, which is an example of a weak assumption in networked systems. In real-world applications, systems handle this using retries, timeouts, or service discovery mechanisms to improve reliability.

## 4. Security Observation
<!-- This TCP exchange has no authentication, no encryption, and
     no message integrity check. Identify one concrete attack that
     is possible against your implementation as written, and explain
     why it works. (~100 words) -->
One possible attack on this TCP implementation is a man-in-the-middle (MITM) attack. Since the communication is not encrypted, an attacker can intercept the messages between the client and server and read or modify them.

This is possible because TCP does not provide encryption or authentication by default. Anyone on the same network can capture packets and see the data being transmitted in plain text. In real-world systems, this is prevented using encryption protocols such as TLS/SSL, which secure communication channels.
## 5. Reflection
<!-- What was the most important thing you learned from implementing
     this? Connect it to one concept from Week 1 lectures. (~75 words) -->
The most important thing I learned from this lab is how client-server communication works using TCP sockets. I understood how data is transmitted between two programs over a network and how each socket primitive plays a role in establishing and managing the connection.

This relates to the concept of reliable communication in distributed systems, where TCP ensures that data is delivered accurately and in order between the client and server.

## References
Tanenbaum, A. & Van Steen, M. (2017). *Distributed Systems: Principles and Paradigms* (3rd ed.). Chapter 4.
# TCP overview 
- ref: https://app.codecrafters.io/concepts/tcp-overview
- TCP builds on IP; IP is a lower-level protocol than TCP 
- TCP relies on IP to route packets between systems 

## IP - Internet's postal service 
- When a program sends data over the network using IP, the data is broken up and sent as multiple "packets".
- Each packet contains:
    - a header section : contains source and destination address (like on envelope)
    - a data section
- The important similarity between IP and postal service is that packets are not guaranteed to arrive at the destination 

## TCP guarantees
- Primarily, TCP offers 2 guarantees: 
1. Reliable delivery of packets
2. In-order delivery of packets

### Reliable Delivery 
- Ensures that no packets are lost in transit 
- By asking the receiver to acknowledge all sent packets and re-transmitting any packets if an acknowledgement isn't received

### In-order Delivery
- Guarantees that the packets are delivered in order
- By labelling each packet with a sequence number 
- The receiver tracks these numbers and reorders out-of-sequence packets
- If a packet is missing, the receiver waits for it to be re-transmitted 

## TCP Connections
- TCP is a connection-oriented protocol 
- To interact over TCP, a program must first establish a connection 
- To establish a connection, one program takes the role of a "server" and the other program takes the role of a "client".
- The server waits for connections, and the client initiates a connection
- Once a connection is established, the client and server can both receive and send data (it's a two-way channel)
- TCP connection is identified using a unique combination of 4 values:
1. destination IP address : e.g. 8.8.8.8 
2. destination port number : e.g. 443 (default port used by https)
3. source IP address : e.g. y.y.y.y (your computer)
4. source port number : e.g. 26789 (free port on your computer)
- If your browser opens multiple connections to Google's server, only the "source port number" will change, the rest will remain the same. 

## TCP Handshake (3-way handshake)
- 3-step process of how clients establish connections with servers 
### Step 1. SYN 
- The client initiates the connection by sending a SYN (synchronize) packet to the server, indicating a request to establish a connection
- This packet also contains a sequence number to maintain the order of the packets being sent 
### Step 2. SYN-ACK
- The server, upon receiving this SYN packet, sends back a SYN-ACK (synchronize-acknowledge) packet
### Step 3. ACK
- The client acknowledges the server's SYN-ACK packet by sending ACK (acknowledge) packet
- The connection is considered established once this last packet is received by the server 

## TCP in python [TODO]
- ref: https://app.codecrafters.io/concepts/python-tcp-server 

- Python's [socket](https://docs.python.org/3/library/socket.html) module provides access to networking primitives.

To write TCP servers in Python, you'll need to be familiar with the following methods:
- [socket.create_connection](https://docs.python.org/3/library/socket.html#socket.create_connection)
- [socket.create_server](https://docs.python.org/3/library/socket.html#socket.create_server)
- [socket.Socket.accept](https://docs.python.org/3/library/socket.html#socket.socket.accept)
- [socket.Socket.recv](https://docs.python.org/3/library/socket.html#socket.socket.recv)
- [socket.Socket.sendall](https://docs.python.org/3/library/socket.html#socket.socket.sendall)

- We'll start by looking at `socket.create_connection` and `socket.create_server` 
- `socket.create_connection` is used to initiate outbound connections.
```python
# Connects to a TCP server running on localhost:8080 and returns the associated socket
client_socket = socket.create_connection(("localhost", 8080))
```

- `socket.create_server` is used to create TCP servers to accept inbound connections.
```python
# Starts a TCP server listening on localhost:8080 and returns the associated socket
server_socket = socket.create_server(("localhost", 8080))
```
- To create a TCP server, pass in a tuple consisting of `(host, port)` as `address`
```python
def create_server(address, *, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False)
```

- Once a server is created using `socket.create_server`, the `socket.Socket.accept` method can be used to accept incoming connections
- `socket.Socket.accept` method blocks execution and waits for an incoming connection 
```python
connection, address = server_socket.accept()
```
- When a client connects, it returns a new [Socket object](https://docs.python.org/3/library/socket.html#socket-objects) representing the connection and a tuple holding the address of the client. 
- This socket object can be used to read and write data to the connection. 

### Reading and writing data
- `socket.Socket.recv` : `def recv(bufsize[, flags])`
    - Reads data from a connection 
    - The maximum amount of data to be received at once is specified by `bufsize`
    - Returns a bytes object with the received data 
    - If an empty bytes object is received, it signals that the client closed the connection 
```python
connection, address = server_socket.accept()
data = connection.recv(1024)
```

- `socket.Socket.sendall` : `def sendall(bytes[, flags])`
    - writes data to a connection
    - data to be written needs to be passed in as a `bytes` object 
    - automatically handles the case where the entire buffer isn't written to the connection in one go 
```python
connection.sendall(b"Hello, client!")
```

-------------------------------------------------------


#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 14/11/2024
import socket

# Simulate the Server (Chef) who directly prepares and serves the dish
def two_tier_server():
    # Create a socket object using IPv4 addressing (AF_INET) and TCP protocol (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the server socket to the local host and port 8080
    server_socket.bind(('localhost', 8080))
    
    
    # Put the server socket into listening mode to accept incoming client connections
    server_socket.listen(1)  # Argument 1 means it can handle 1 connection at a time
    print("Chef (Server) is ready to take orders...")
    
    while True:
        # Accept a connection from the client
        conn, addr = server_socket.accept()
        print(f"Order received from {addr} (Client)")
        
        # Receive data from the client through the connection socket (conn)
        data = conn.recv(1024).decode()  # Read up to 1024 bytes and decode to a string
        
        # Check if any data was received from the client
        if data:
            print(f"Chef received the order: {data}")
            # Send a response to the client
            conn.sendall(b"Dish is ready! Served by the Chef (Server)")
        
        # Close the connection
        conn.close()
        break  # End the server after one interaction for simplicity

# Simulate the Client (Customer) placing an order directly with the chef
def two_tier_client():
    # Create a socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the client socket to the server (Chef) on localhost and port 8080
    client_socket.connect(('localhost', 8080))
    
    # Send an order to the server
    client_socket.sendall(b"Customer orders a dish")
    
    # Receive the response from the server
    response = client_socket.recv(1024).decode()  # Decode the server's response
    print(f"Customer recieved: {response}")
    
    # Close the client socket
    client_socket.close()

# Run the server and client for testing purposes
if __name__ == "__main__":
    # Run the server in a separate process or thread in actual usage
    # For demonstration, we call them sequentially here
    two_tier_server()  # Start the server
    two_tier_client()  # Start the client

#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 14/11/2024
import socket
import concurrent.futures


# Define the server function to simulate the Chef
def two_tier_server():
    # Create a server socket using IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))  # Bind to localhost on port 8080
    server_socket.listen(5)  # Allow up to 5 incoming connections in the queue
    print("Chef (Server) is ready to take orders...")

    while True:
        # Accept client connections
        conn, addr = server_socket.accept()
        print(f"Order received from {addr} (Client)")

        # Receive data from the client
        data = conn.recv(1024).decode()
        if data:
            print(f"Chef received the order: {data}")
            # Send a response back to the client
            conn.sendall(b"Dish is ready! Served by the Chef (Server)")
        
        # Close the connection after the order is processed
        conn.close()


# Define the client function to simulate the Customer
def two_tier_client(client_id):
    # Create a client socket using IPv4 and TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))  # Connect to the server on localhost and port 8080

    # Send an order to the server
    message = f"Customer {client_id} orders a dish"
    client_socket.sendall(message.encode())

    # Receive the server’s response
    response = client_socket.recv(1024).decode()
    print(f"Customer {client_id} received: {response}")

    # Close the client socket
    client_socket.close()



if __name__ == "__main__":
    # Start the server in a separate thread
    with concurrent.futures.ThreadPoolExecutor() as executor:
        server_future = executor.submit(two_tier_server)

        # Simulate multiple clients placing orders concurrently
        client_ids = range(1, 6)  # Simulate 5 clients
        client_futures = [executor.submit(two_tier_client, client_id) for client_id in client_ids]

        # Wait for all clients to finish
        for future in concurrent.futures.as_completed(client_futures):
            future.result()

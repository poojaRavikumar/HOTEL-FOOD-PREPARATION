#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 14/11/2024
import socket
import threading

# Define a function to simulate a peer (Chef)
def peer(peer_name, port, target_port=None, message=None):
    # Create a socket for the peer
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peer_socket.bind(('localhost', port))  # Bind to localhost and a specified port
    peer_socket.listen(1)  # Listen for one incoming connection
    print(f"{peer_name} is ready to collaborate...")

    # If a target port and message are provided, send a task to another peer
    if target_port and message:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', target_port))  # Connect to the target peer
        client_socket.sendall(message.encode())  # Send the message/task
        response = client_socket.recv(1024).decode()  # Receive the response
        print(f"{peer_name} received: {response}")
        client_socket.close()

    # Accept incoming connections from other peers
    conn, addr = peer_socket.accept()
    print(f"{peer_name} connected with {addr}")

    # Receive data (task) from the connected peer
    data = conn.recv(1024).decode()
    if data:
        print(f"{peer_name} received task: {data}")
        # Send a response back indicating the task completion
        conn.sendall(f"{peer_name} completed the task and sent back the result".encode())
    
    conn.close()
    peer_socket.close()

# Run two peers (Chefs) that collaborate directly
if __name__ == "__main__":
    peer1_port = 8080  # Port for the first peer
    peer2_port = 8084  # Port for the second peer

    # Start both peers in separate threads
    thread1 = threading.Thread(target=peer, args=("Chef1", peer1_port, peer2_port, "Task: Prepare Salad"))
    thread2 = threading.Thread(target=peer, args=("Chef2", peer2_port))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

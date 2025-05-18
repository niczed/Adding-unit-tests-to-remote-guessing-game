import socket

def start_client():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to the game server!")

        while True:
            guess = input("Enter your guess (1-100): ")
            s.sendall(guess.encode())
            data = s.recv(1024).decode()
            print("Server says:", data)
            if data == "Correct":
                break

if __name__ == "__main__":
    start_client()

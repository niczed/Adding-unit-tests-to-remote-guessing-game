from game import evaluate_guess  # Make sure this file is named correctly

def start_server(number_to_guess=None):
    import socket
    import random

    host = '127.0.0.1'
    port = 65432
    number_to_guess = number_to_guess or random.randint(1, 100)

    print(f"[INFO] Server starting...")
    print(f"[DEBUG] Number to guess is: {number_to_guess}")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"[INFO] Server is listening on {host}:{port}")

            conn, addr = s.accept()
            with conn:
                print(f"[INFO] Connected by {addr}")
                while True:
                    data = conn.recv(1024).decode()
                    if not data:
                        print("[INFO] No data received. Closing connection.")
                        break
                    print(f"[DEBUG] Received guess: {data}")
                    guess = int(data)
                    response = evaluate_guess(guess, number_to_guess)
                    print(f"[DEBUG] Sending response: {response}")
                    conn.sendall(response.encode())

    except Exception as e:
        print(f"[ERROR] {e}")

# ✅ ENTRY POINT
if __name__ == "__main__":
    start_server()

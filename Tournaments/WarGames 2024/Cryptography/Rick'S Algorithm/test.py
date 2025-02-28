import socket

# Server details
host = "43.217.80.203"
port = 33460

# Create a socket to connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

def send_and_receive(data):
    # Send data to the server
    sock.sendall(data.encode())
    
    # Receive the response from the server
    response = sock.recv(4096).decode()
    return response

# Start interacting with the challenge server
try:
    while True:
        # Read the server's prompt
        server_prompt = sock.recv(1024).decode()
        print("Server Prompt:", server_prompt)

        # If the prompt asks for a choice, send the option
        if "Enter option:" in server_prompt:
            # Send option 3 to print the encrypted flag or n
            option = "3"  # This might be the option to print the encrypted flag or n
            print(f"Sending option: {option}")
            server_response = send_and_receive(option)
            print("Server Response:", server_response)

        # If the prompt includes the value of n, try to extract it
        if "n =" in server_response:
            n_value = server_response.split("n =")[1].split()[0].strip()
            print("Extracted n value:", n_value)
            break  # You can break after extracting n or continue with further actions

except Exception as e:
    print("Error:", e)

finally:
    # Close the connection after interaction
    sock.close()

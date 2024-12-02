from flask import Flask, render_template, request
import socket

app = Flask(__name__)

# Function to handle sending the "ping" to the server
def send_ping():
    try:
        # Use the Replit public URL as the host (Replace this with the actual server URL)
        host = "216.24.57.4"  # Replace with your Replit server's URL
        port = 10000  # Port the server is listening on

        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(client_socket)

        # Connect to the server
        client_socket.connect((host, port))
        print(client_socket)

        # Send the "ping" message
        message = "ping"
        client_socket.send(message.encode('utf-8'))

        # Receive the response from the server
        response = client_socket.recv(1024).decode('utf-8')

        # Close the socket
        client_socket.close()

        return response
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        # Send ping when the button is pressed
        response = send_ping()
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

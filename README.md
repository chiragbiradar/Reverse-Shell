# Reverse Shell
The Reverse Shell is a versatile tool that allows remote connections to personal computers across the globe. It leverages the concept of reverse connections, which enables users to connect to someone's PC and provide assistance or perform actions remotely.

# Key Features
Connect to remote computers for troubleshooting or assistance.
Enables remote access without the user's knowledge (for educational purposes only).
Multiple client support for controlling multiple computers from a single server.
Command prompt or terminal interface for listing connected clients, selecting a client, and sending commands.
Threading implementation for handling simultaneous tasks.

# How It Works
The Reverse Shell program consists of two main tasks performed concurrently using threading:

* Task 1: Listening and accepting connections from clients, storing them in a list.
* Task 2: Sending commands to connected clients and managing remote access.
The program sets up two threads to handle these tasks efficiently. The first thread continuously listens for incoming connections, accepts them, and stores the associated connection data in a list. The second thread handles interaction with connected clients, allowing users to select a specific client and send commands to that computer remotely.

# Usage
1. Clone the repository to your local machine:

2. Choose the appropriate version of the reverse shell based on your needs:
 * For a single client:
   - Open client.py and modify the IP address to the server's IP address.
   - Run client.py on the target machine.
* For multiple clients:
  - Open client.py and modify the IP address to the server's IP address.
  - Run client.py on each target machine.

3. Set up the server:
* Run server.py on the machine that will act as the server.
* Preferably, use a static IP address (e.g., cloud servers) for the server.
* Note: Ensure that the target machine(s) can establish a network connection with the server.


# Disclaimer
This project is intended for educational purposes only. The Reverse Shell should be used responsibly and ethically. Unauthorized access to computers without proper consent is illegal.

# Contribution
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

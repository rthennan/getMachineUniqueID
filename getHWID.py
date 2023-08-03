import socket

def get_host_name():
    return socket.gethostname()

def get_computer_name():
    return socket.getfqdn()

host_name = get_host_name()
computer_name = get_computer_name()

print(f"Host Name: {host_name}")
print(f"Computer Name: {computer_name}")

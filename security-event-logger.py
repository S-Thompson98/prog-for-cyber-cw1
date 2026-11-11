#security-event-logger

import os
from datetime import datetime

# Correct login details
correct_username = "admin"
correct_password = "password123"

# Store event logs
event_log = []


# Function to generate random Event ID
def generate_event_id():
    return int.from_bytes(os.urandom(2), "big") % 9000 + 1000


# Function to generate random IP address
def generate_ip():
    return ".".join(
        str(int.from_bytes(os.urandom(1), "big") % 256)
        for _ in range(4)
    )


# Function to generate timestamp
def generate_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Function to check login details
def check_login(username, password):
    if username == correct_username and password == correct_password:
        return "Successful login"
    else:
        return "Failed login"


# Function to record login attempt
def record_event(username, event):
    log = {
        "Event ID": generate_event_id(),
        "Username": username,
        "IP Address": generate_ip(),
        "Event": event,
        "Timestamp": generate_timestamp()
    }

    event_log.append(log)


# Function to display security event log
def display_event_log():
    print("\nSECURITY EVENT LOG")
    print("==================")

    for log in event_log:
        print("Event ID:", log["Event ID"])
        print("Username:", log["Username"])
        print("IP Address:", log["IP Address"])
        print("Event:", log["Event"])
        print("Timestamp:", log["Timestamp"])
        print()


# Main login function
def login_system():
    while True:
        username = input("\nEnter username: ")
        password = input("Enter password: ")

        event = check_login(username, password)

        record_event(username, event)

        display_event_log()

        if event == "Successful login":
            print("Login successful! Access granted.")
            break
        else:
            print("Incorrect username or password. Please try again.")


# Run the program
if __name__ == "__main__":
    login_system()
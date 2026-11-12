#security incident-manager
#SThompson
#B01886612

import os
from datetime import datetime

# Correct login details
correct_username = "admin"
correct_password = "password123"

# Store security logs
security_logs = []


# Function to generate Event ID
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


# Function to create security incident tuple
def create_security_record(username, ip, event, severity):
    return (username, ip, event, severity)


# Function to record security event
def record_event(username, event):
    event_id = generate_event_id()
    ip_address = generate_ip()
    timestamp = generate_timestamp()

    # Set severity level
    if event == "Failed login":
        severity = "High"
    else:
        severity = "Low"

    # Create tuple
    incident = create_security_record(
        username, ip_address, event, severity
    )

    # Store complete event log
    log = {
        "Event ID": event_id,
        "Incident": incident,
        "Timestamp": timestamp
    }

    security_logs.append(log)


# Function to display event log
def display_event_log():
    print("\nSECURITY EVENT LOG")
    print("==================")

    for log in security_logs:
        incident = log["Incident"]

        print("Event ID:", log["Event ID"])
        print("Username:", incident[0])
        print("IP Address:", incident[1])
        print("Event:", incident[2])
        print("Severity:", incident[3])
        print("Timestamp:", log["Timestamp"])
        print()


# Function to demonstrate tuple operations
def tuple_details(incident):
    print("\nSECURITY INCIDENT TUPLE")
    print("=======================")

    print("Username:", incident[0])
    print("IP Address:", incident[1])
    print("Event Type:", incident[2])
    print("Severity:", incident[3])

    print("Number of elements:", len(incident))

    if "Failed login" in incident:
        print("Failed login event found.")
    else:
        print("Failed login event not found.")

    # Demonstrate tuple immutability
    try:
        incident[0] = "user"
    except TypeError:
        print("Tuples cannot be modified!")


# Function to demonstrate dictionary operations
def dictionary_details(incident):
    # Populate dictionary using tuple information
    security_incident = {
        "username": incident[0],
        "IP address": incident[1],
        "event type": incident[2],
        "risk level": incident[3]
    }

    # Display username and IP address
    print("\nSECURITY INCIDENT DICTIONARY")
    print("============================")
    print("Username:", security_incident["username"])
    print("IP Address:", security_incident["IP address"])

    # Add a new status field
    security_incident["status"] = "Under investigation"

    # Update risk level
    if incident[2] == "Failed login":
        security_incident["risk level"] = "Critical"
    else:
        security_incident["risk level"] = "Low"

    # Remove the event type field
    del security_incident["event type"]

    # Display remaining keys and values
    print("\nRemaining dictionary information:")

    for key, value in security_incident.items():
        print(key, ":", value)

    # Display keys and values
    print("\nDictionary keys:")
    print(security_incident.keys())

    print("\nDictionary values:")
    print(security_incident.values())

    # Count dictionary elements
    print("\nTotal key-value pairs:", len(security_incident))


# Main login system
def login_system():
    while True:
        username = input("\nEnter username: ")
        password = input("Enter password: ")

        # Check login details
        event = check_login(username, password)

        # Record login attempt
        record_event(username, event)

        # Display all security logs
        display_event_log()

        if event == "Successful login":
            print("Login successful! Access granted.")
            break
        else:
            print("Incorrect username or password. Try again.")

    # Get the latest security incident
    latest_incident = security_logs[-1]["Incident"]

    # Run tuple and dictionary tasks
    tuple_details(latest_incident)
    dictionary_details(latest_incident)


# Run the complete program
if __name__ == "__main__":
    login_system()

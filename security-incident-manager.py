#security incident-manager
#SThompson
#B01886612

import os
from datetime import datetime

correct_username = "admin"
correct_password = "password123"
#generate a random event ID using os.urandom and convert it to a hexadecimal string
def generate_event_id():
    return int.from_bytes(os.urandom(2), "big") % 9000 + 1000

#generate a random IP address using os.urandom and convert it to a string in the format of xxx.xxx.xxx.xxx
def generate_ip_address():
    return ".".join(str(int.from_bytes(os.urandom(1), "big") % 256) for _ in range(4))

#generate a timestamp using the datetime module and format it as YYYY-MM-DD HH:MM:SS
def generate_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#function to check if the username and password are correct
def check_login(username, password):
    if username == correct_username and password == correct_password:
        return "Successful login"
    else:
        return "Failed login"

#function to record the login attempt in the event log
def record_event(username, event):
    log = {
        "Event ID": generate_event_id(),
        "Username": username,
        "IP Address": generate_ip_address(),
        "Event": event,
        "Timestamp": generate_timestamp()
    }
    event_log.append(log)

#function to display the security event log
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

#function to run the login system
def login_system():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        event = check_login(username, password)
        record_event(username, event)
        print(event)
        display_event_log()
        repeat = input("Do you want to try again? (yes/no): ").strip().lower()
        if repeat != "yes":
            break
# Run the program
if __name__ == "__main__":
    event_log = []
    login_system()

input("Press Enter to exit...")
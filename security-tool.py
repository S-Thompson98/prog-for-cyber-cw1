#S-Thompson
#B01886612
#security-tool

# SECURITY TOOL

# Store the correct username and password
correct_username = "admin"
correct_password = "Pa$$w0rd"

# FUNCTION 1: LOGIN AUTHENTICATION

def login_authentication():

    print("\nUSER LOGIN")

    # Set the maximum number of failed attempts
    max_attempts = 3

    # Initialise the failed login counter
    failed_attempts = 0

    # Ask for login details until successful or attempts run out
    while failed_attempts < max_attempts:

        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check whether the credentials are correct
        if username == correct_username and password == correct_password:

            print("\nAuthentication successful!")
            print("Welcome to the Security Tool.")

            return True

        else:

            # Increase the failed login counter
            failed_attempts += 1

            print("\nAuthentication failed!")
            print("Failed attempts:", failed_attempts)
            print("Attempts remaining:", max_attempts - failed_attempts)

    # Display account freeze message
    print("\nMaximum login attempts reached!")
    print("Your account is frozen for 24 hours.")

    return False


# FUNCTION 2: SECURITY EVENT COUNTER

def security_event_counter():

    # Initialise password counters
    correct_count = 0
    incorrect_count = 0

    print("\nSecurity Event Counter")

    # Ask the user to enter a password 10 times
    for i in range(10):

        password = input(f"Enter password ({i+1}/10): ")

        # Check whether the password is correct
        if password == correct_password:
            correct_count += 1
            print("Correct password!")

        else:
            incorrect_count += 1
            print("Incorrect password!")

    # Calculate incorrect password percentage
    percentage = (incorrect_count / 10) * 100

    # Display the security report
    print("\nSecurity Report")
    print("Correct passwords:", correct_count)
    print("Incorrect passwords:", incorrect_count)
    print("Percentage of incorrect passwords:", percentage, "%")

    # Raise an alert if incorrect passwords exceed 50%
    if percentage > 50:
        print("ALERT! More than 50% of passwords are incorrect!")

    else:
        print("Security level acceptable.")


# FUNCTION 3: BRUTE-FORCE SIMULATION

def brute_force_simulation():

    print("\nBrute-Force Simulation")

    # Set the predefined password
    predefined_password = "Pa$$w0rd"

    # Set the maximum number of attempts
    max_attempts = 5

    # Initialise the attempt counter
    attempts = 0

    # Continue until the password is guessed or attempts run out
    while attempts < max_attempts:

        guess = input("Guess the password: ")

        # Increase the attempt counter
        attempts += 1

        # Check whether the guess is correct
        if guess == predefined_password:

            print("Password cracked successfully!")
            print("Attempts used:", attempts)

            break

        else:

            print("Incorrect guess!")
            print("Attempts remaining:", max_attempts - attempts)

    # Check whether maximum attempts have been reached
    if attempts == max_attempts and guess != predefined_password:

        print("Maximum attempts reached!")
        print("Brute-force simulation stopped.")
#display the percentage of incorrect guesses
    if attempts == max_attempts:
        incorrect_percentage = (attempts / max_attempts) * 100
        print("Percentage of incorrect guesses:", incorrect_percentage, "%")

# FUNCTION 4: DISPLAY MENU

def display_menu():

    # Display the main menu options
    print("\nSECURITY TOOL")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")


# FUNCTION 5: MAIN PROGRAM

def main():

    # Authenticate the user before displaying the menu
    authenticated = login_authentication()

    # Only continue if authentication is successful
    if authenticated == True:

        # Keep displaying the menu until the user exits
        while True:

            display_menu()

            # Ask the user to select an option
            choice = input("Enter your choice (1-4): ")

            # Call the Security Event Counter function
            if choice == "1":
                security_event_counter()

            # Call the Brute-Force Simulation function
            elif choice == "2":
                brute_force_simulation()

            # Allow the user to authenticate again
            elif choice == "3":

                if login_authentication() == False:
                    break

            # Exit the program
            elif choice == "4":

                print("\nThank you for using the security tool")
                break

            # Handle invalid menu selections
            else:
                print("Invalid choice! Please select an option from 1 to 4.")

    else:

        # Deny access if initial authentication fails
        print("\nAccess denied. Security Tool is unavailable.")


# START THE PROGRAM
if __name__ == "__main__":
    main()



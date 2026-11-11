# Import the security_tools module
# This allows us to use the functions from security_tools.py

import security_tools


# Main function to run the password and IP address checker
def main():

    # Give the user three attempts to enter a valid password and IP address
    for i in range(3):

        # Ask the user to enter a password
        password = input("Enter a password: ")

        # Ask the user to enter an IP address
        ip_address = input("Enter an IP address: ")

        # Check if the password is strong enough and the IP address is valid
        if (security_tools.check_password_strength(password)
                and security_tools.validate_ip_address(ip_address)):

            # Display a success message if both checks pass
            print("\nPassword is strong enough!")
            print("IP address is valid!")

            # End the program because both entries are correct
            return

        else:

            # Display an error message if either check fails
            print("\nPassword is not strong enough or IP address is invalid.")

            # Tell the user how many attempts they have remaining
            if i < 2:
                print(f"You have {2 - i} attempts remaining.")

    # This section runs if the user fails all three attempts
    print("\nYou have failed all three attempts.")

    # Inform the user that random alternatives are being generated
    print("Generating a random password and IP address...")

    # Call the function from security_tools.py to generate a strong password
    random_password = security_tools.generate_random_password()

    # Call the function from security_tools.py to generate an IP address
    random_ip = security_tools.generate_random_ip()

    # Display the randomly generated password and IP address
    print("\n--- GENERATED DETAILS ---")
    print("Random password:", random_password)
    print("Random IP address:", random_ip)
    print("-------------------------")

#a function that asks the user if they want to restart the program and if they do it will call the main function again
def restart_program():
    restart = input("\nDo you want to restart the program? (y/n): ")
    if restart.lower() == "y":
        main()
    else:
        print("Goodbye!")
# Check whether this file is being run directly
if __name__ == "__main__":

    # Run the main function
    main()
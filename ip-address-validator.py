#ip address validator
#Sthompson
#B01886612

#This function is to check if the ip address is valid or not
def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

#The main function to run the program
def main():
    ip_address = input("Enter an IP address: ")
    if is_valid_ip(ip_address):
        print(f"{ip_address} is a valid IP address.")
    else:
        print(f"{ip_address} is not a valid IP address.")

# a function to ask if the user wants to repeat the program
def repeat_program():
    while True:
        repeat = input("Do you want to check another IP address? (yes/no): ").strip().lower()
        if repeat == 'yes':
            main()
        elif repeat == 'no':
            print("Exiting the program.")
            break
        else:
            print("Please enter 'yes' or 'no'.")
if __name__ == "__main__":
    main()
    repeat_program()

input("Press Enter to exit...")
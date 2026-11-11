import random
import os
import string
#functions to check if the passord is strong enough to be used for security purposes
def check_password_strength(password):
    #check if the password is at least 10 characters long
    if len(password) < 10:
        return False
    
    #check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    #check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    #check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    #check if the password contains at least one special character
    special_characters = "!@#$%^&*"
    if not any(char in special_characters for char in password):
        return False
    
    #if the password meets all the criteria, return True
    return True

#a function to validate IP address
def validate_ip_address(ip):
    #split the IP address into its four octets
    octets = ip.split(".")
    
    #check if there are exactly four octets
    if len(octets) != 4:
        return False
    
    #check if each octet is a number between 0 and 255
    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return False
    
    #if the IP address is valid, return True
    return True

#a function to generate a random password that meed the criteria for a strong password
def generate_random_password(length=12):
    #define the character sets to use for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*"
    
    #combine all character sets into one
    all_characters = lowercase + uppercase + digits + special_characters
    
    #generate a random password of the specified length
    password = "".join(random.choice(all_characters) for _ in range(length))
    
    #check if the generated password meets the strength criteria
    while not check_password_strength(password):
        password = "".join(random.choice(all_characters) for _ in range(length))
    
    return password

def generate_random_ip():
    #generate a random IP address
    return ".".join(str(random.randint(0, 255)) for _ in range(4))
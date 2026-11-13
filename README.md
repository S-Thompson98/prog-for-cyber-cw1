# Task 5 – Reusable Cyber Security Utilities Using User-Defined Modules

## Student Information

- **Name:** Stephen Thompson
- **Campus:** New College Lanarkshire
- **Banner ID:** B01886612

## Project Description

This project involves developing a collection of reusable Cyber Security utilities using Python user-defined modules.

Instead of writing all the program functionality in one Python file, the project separates reusable functions into a module called `security_tools.py`.

A second file called `main.py` imports the module and uses its functions to validate passwords, check IP addresses and generate strong random passwords.

## How to Run the Program

1. Open the GitHub repository.
2. Select the `cyber-security-utilities` branch.
3. Open the project in Visual Studio Code.
4. Make sure that both `main.py` and `security_tools.py` are saved in the same directory.
5. Open the `main.py` file.
6. Run the Python program.
7. Enter a password when prompted.
8. Enter an IP address when prompted.
9. Review the validation results.
10. If the password is not strong enough, review the suggested generated password.

**Important:** Run `main.py` rather than `security_tools.py`, because `main.py` imports and uses the functions from the module.

## Testing and Evidence

Here is the testing used:

### Password Testing

- Enter a password that meets all requirements.
- Enter a password that is too short.
- Enter a password without a digit.
- Enter a password without a symbol.
- Enter a password without a letter.
- Check that a suggested strong password is generated when required.

### IP Address Testing

- Enter a valid IP address.
- Enter an IP address with an incorrect number of dots.
- Enter an IP address with fewer than four octets.
- Enter an IP address containing letters.
- Enter an IP address with an octet greater than 255.

### Password Generator Testing

- Generate multiple passwords.
- Check that generated passwords have a length between 10 and 16 characters.
- Check that generated passwords contain uppercase letters, lowercase letters, digits and symbols.

Screenshots provided in branch.


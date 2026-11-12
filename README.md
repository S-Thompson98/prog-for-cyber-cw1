# Task 5 – Reusable Cyber Security Utilities Using User-Defined Modules

## Student Information

- **Name:** Stephen Thompson
- **Campus:** New College Lanarkshire
- **Banner ID:** B01886612

## Project Description

This project involves developing a collection of reusable Cyber Security utilities using Python user-defined modules.

Instead of writing all the program functionality in one Python file, the project separates reusable functions into a module called `security_tools.py`.

A second file called `main.py` imports the module and uses its functions to validate passwords, check IP addresses and generate strong random passwords.

## Program Features

### 1. Password Validation

The program includes a function that checks whether a password meets basic security requirements.

The password validation function checks:

- Whether the password meets the minimum required length.
- Whether the password contains at least one letter.
- Whether the password contains at least one digit.
- Whether the password contains at least one symbol.
- Whether the password meets the required password variety.

### 2. IP Address Validation

The program includes another function that performs basic IP address validation.

The function checks:

- Whether the IP address contains exactly three dots.
- Whether the IP address contains four numerical octets.
- Whether all octets contain valid numbers.
- Whether each octet is between 0 and 255.

### 3. Strong Random Password Generator

The program includes a function that generates a strong random password.

The password generator:

- Generates a random password length between 10 and 16 characters.
- Uses uppercase letters.
- Uses lowercase letters.
- Includes numerical digits.
- Includes special symbols.
- Generates a different random password when called.

### 4. Main Python Program

The `main.py` file performs the following operations:

- Imports the `security_tools` module.
- Asks the user to enter a password.
- Asks the user to enter an IP address.
- Calls the password validation function.
- Calls the IP address validation function.
- Displays the validation results.
- Suggests a randomly generated strong password if the entered password does not meet the requirements.

## Project Structure

The project contains two main Python files:

```text
cyber-security-utilities/
│
├── main.py
├── security_tools.py
├── README.md
├── LICENSE
│
└── screenshots/
```

### File Descriptions

**1. security_tools.py**

- Contains reusable cyber security functions.
- Includes password validation.
- Includes IP address validation.
- Includes strong random password generation.

**2. main.py**

- Imports the `security_tools` module.
- Collects user input.
- Calls the functions from the module.
- Displays the results to the user.

## Python Concepts Used

- User-defined functions.
- Python modules.
- Import statements.
- Function parameters.
- Return values.
- String operations.
- Conditional statements.
- Random number generation.
- Password validation.
- IP address validation.
- Code reusability.

## Technologies Used

- Python 3.
- Visual Studio Code.
- Git and GitHub.

## Project Files

- `main.py` – Main Python program.
- `security_tools.py` – Reusable cyber security functions.
- `README.md` – Project documentation.
- `LICENSE` – Repository licence.
- `screenshots/` – Testing screenshots.

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

Alternatively, open the terminal in the project directory and run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

**Important:** Run `main.py` rather than `security_tools.py`, because `main.py` imports and uses the functions from the module.

## Testing and Evidence

The program should be tested using different passwords and IP addresses.

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

Screenshots of the testing results will be saved in the `screenshots/` folder.

## GitHub Branch

- **Branch Name:** `cyber-security-utilities`
- **Task Number:** Task 5

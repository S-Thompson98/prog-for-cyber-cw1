# Task 5 – Reusable Cyber Security Utilities Using User-Defined Modules

## Student Information

- **Name:** Stephen Thompson
- **Campus:** New College Lanarkshire
- **Banner ID:** B01886612

## Project Description

This project involves developing a collection of reusable Cyber Security utilities using Python user-defined modules.

Instead of writing all the program functionality in one Python file, the project separates reusable functions into a module called `security_tools.py`.

A second file called `main.py` imports the module and uses its functions to validate passwords, check IP addresses and generate strong random passwords.

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

Screenshots provided in branch.

## GitHub Branch

- **Branch Name:** `cyber-security-utilities`
- **Task Number:** Task 5

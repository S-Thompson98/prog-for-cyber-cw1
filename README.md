# Task 1 – Security Tool

## Student Information

- **Name:** Stephen thompson
- **Campus:** New College Lanarkshire 
- **Banner ID:** B01886612

## Project Description

This project involves developing a basic security tool for a small organisation using Python.

The program requires the user to authenticate before accessing a security menu. After successful authentication, the user can select different security functions.

The program continues running until the user chooses the Exit option.

## Program Features

### 1. Security Event Counter

- Asks the user to enter a password ten times.
- Compares each entered password with a predefined correct password.
- Counts the number of correct password entries.
- Counts the number of incorrect password entries.
- Calculates the percentage of incorrect password entries.
- Displays an alert if the percentage of incorrect entries exceeds 50%.

### 2. Brute-Force Simulation

- Uses a predefined password.
- Allows the user to enter password guesses.
- Counts the number of attempts.
- Stops when the correct password is entered.
- Stops when the maximum number of attempts is reached.

### 3. Login Authentication

- Requests a username and password.
- Checks whether the entered credentials are correct.
- Displays whether authentication was successful or unsuccessful.
- Allows the user to try again after an unsuccessful login.
- Allows a maximum of three failed login attempts.
- Displays a message stating that the account is frozen for 24 hours after the maximum number of failed attempts.

### 4. Exit

- Allows the user to exit the security tool.
- Displays the message:

  "Thank you for using the security tool".

## Python Concepts Used

- Variables and data types.
- User input and output.
- Conditional statements (`if`, `elif`, `else`).
- Loops (`while` and `for`).
- Counters.
- Mathematical calculations.
- Input validation.
- Exception handling using `try-except` where appropriate.

## Technologies Used

- Python 3.
- Visual Studio Code.
- Git and GitHub.

## Project Files

- `security_tool.py` – Main Python program.
- `README.md` – Project documentation.
- `LICENSE` – Repository licence.
- `screenshots/` – Testing screenshots.

## How to Run the Program

1. Open the GitHub repository.
2. Select the `security-tool` branch.
3. Open the project in Visual Studio Code.
4. Open the `security_tool.py` file.
5. Run the Python program.
6. Follow the instructions displayed in the terminal.
7. Enter the required login credentials to access the security menu.

Alternatively, run the program using the terminal:

```bash
python security_tool.py
```

On some systems, use:

```bash
python3 security_tool.py
```

## Testing and Evidence

The program should be tested using different inputs.

Testing should include:

- Successful initial authentication.
- Incorrect initial authentication.
- Correct and incorrect password entries in the security event counter.
- An incorrect password percentage greater than 50%.
- Successful brute-force password guessing.
- Reaching the maximum brute-force attempts.
- Successful login authentication.
- Three consecutive failed login attempts.
- Selecting the Exit option.

Screenshots of the program outputs will be saved in the `screenshots/` folder.

## GitHub Branch

- **Branch Name:** `security-tool`
- **Task Number:** Task 1

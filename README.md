# Task 2 – Security Event Logger

## Student Information

- **Name:** Stephen Thompson
- **Campus:** New College Lanarkshire
- **Banner ID:** B01886612

## Project Description

This project involves developing a basic Security Event Logger using Python.

A security event logger records security-related activities so they can be reviewed later.

The program asks the user to enter a username and password until the correct credentials are provided.

Every login attempt is recorded and displayed as an event log, including both failed and successful login attempts.

## Program Features

### 1. User Authentication

- Requests a username from the user.
- Requests a password from the user.
- Compares the entered credentials with the correct credentials.
- Continues asking for credentials until the correct username and password are entered.

### 2. Event Logging

The program records information for every login attempt.

The event log includes:

- Event ID.
- Username.
- IP address, where included in the implementation.
- Event description.
- Timestamp.

### 3. Failed Login Attempts

- Detects incorrect login credentials.
- Records each unsuccessful login attempt.
- Displays the relevant event information.
- Continues requesting credentials.

### 4. Successful Login Attempt

- Detects when the correct username and password are entered.
- Records the successful login event.
- Displays the successful authentication event log.

## Example Event Log

The program should display event information in a readable format similar to the following:

```text
Event ID: 3971
Username: admin
IP Address: 192.168.1.25
Event: Failed login
Timestamp: 2026-09-27 01:35:42
```

The actual event information will depend on the values used in the program.

## Python Concepts Used

- Variables and data types.
- User input and output.
- Conditional statements.
- Loops.
- Counters.
- String formatting.
- Date and time handling.
- Basic authentication logic.

## Technologies Used

- Python 3.
- Visual Studio Code.
- Git and GitHub.

## Project Files

- `security_event_logger.py` – Main Python program.
- `README.md` – Project documentation.
- `LICENSE` – Repository licence.
- `screenshots/` – Testing screenshots.

## How to Run the Program

1. Open the GitHub repository.
2. Select the `security-event-logger` branch.
3. Open the project in Visual Studio Code.
4. Open the `security_event_logger.py` file.
5. Run the program.
6. Enter a username and password when requested.
7. Review the event log displayed after each login attempt.
8. Continue until the correct credentials are entered.

Alternatively, use the terminal:

```bash
python security_event_logger.py
```

On some systems, use:

```bash
python3 security_event_logger.py
```

## Testing and Evidence

The program should be tested using different login attempts.

Testing should include:

- Entering an incorrect username.
- Entering an incorrect password.
- Entering both an incorrect username and password.
- Performing multiple failed login attempts.
- Entering the correct username and password.
- Checking that every attempt produces an event log.
- Checking that event IDs and timestamps are displayed correctly.

Screenshots of the testing results will be saved in the `screenshots/` folder.

## GitHub Branch

- **Branch Name:** `security-event-logger`
- **Task Number:** Task 2

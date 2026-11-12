# Task 4 – Security Incident Manager Using Dictionaries

## Student Information

- **Name:** Stephen thompson
- **Campus:** New College Lanarkshire
- **Banner ID:** B01886612

## Project Description

This project involves creating a basic Security Incident Manager using Python dictionaries.

A dictionary is used to store information about a security incident. The program demonstrates how dictionary information can be accessed, added, updated and removed.

The purpose of this exercise is to understand how Python dictionaries can be used to organise and manage security-related information.

## Program Features

### 1. Creating a Security Incident Dictionary

The program creates a dictionary containing the following information:

- Username.
- IP address.
- Event type.
- Risk level.

### 2. Displaying Incident Information

- Displays the username stored in the dictionary.
- Displays the IP address associated with the incident.

### 3. Adding a New Field

- Adds a new dictionary key called `status`.
- Assigns an appropriate value to the status field.

### 4. Updating the Risk Level

- Accesses the existing risk level.
- Updates the risk level with a new value.

### 5. Removing a Dictionary Field

- Removes one field from the dictionary.
- Updates the dictionary after the removal.

### 6. Displaying Dictionary Information

- Displays all remaining dictionary keys.
- Displays their corresponding values.
- Uses iteration to display the dictionary contents.

### 7. Counting Dictionary Entries

- Calculates the total number of key-value pairs.
- Displays the total using the `len()` function.

## Example Dictionary Structure

The incident information will follow a structure similar to this:

```python
incident = {
    "username": "admin",
    "ip_address": "192.168.1.10",
    "event_type": "Failed Login",
    "risk_level": "High"
}
```

The actual values and dictionary operations will be implemented in the Python program.

## Python Concepts Used

- Dictionaries.
- Dictionary keys and values.
- Adding dictionary entries.
- Updating dictionary values.
- Removing dictionary entries.
- Dictionary iteration.
- The `len()` function.
- Variables and data types.
- Comments.

## Technologies Used

- Python 3.
- Visual Studio Code.
- Git and GitHub.

## Project Files

- `security_incident_manager.py` – Main Python program.
- `README.md` – Project documentation.
- `LICENSE` – Repository licence.
- `screenshots/` – Testing screenshots.

## How to Run the Program

1. Open the GitHub repository.
2. Select the `security-incident-manager` branch.
3. Open the project in Visual Studio Code.
4. Open the `security_incident_manager.py` file.
5. Run the Python program.
6. Review the displayed incident information.
7. Observe how the dictionary changes after each operation.

Alternatively, use the terminal:

```bash
python security_incident_manager.py
```

On some systems, use:

```bash
python3 security_incident_manager.py
```

## Testing and Evidence

The program should be tested to confirm that all dictionary operations work correctly.

Testing should include:

- Creating the initial incident dictionary.
- Displaying the username and IP address.
- Adding the status field.
- Updating the risk level.
- Removing one dictionary field.
- Displaying all remaining keys and values.
- Checking the total number of key-value pairs.

Screenshots of the testing results will be saved in the `screenshots/` folder.

## GitHub Branch

- **Branch Name:** `security-incident-manager`
- **Task Number:** Task 4

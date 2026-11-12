# Task 3 – IP Address Validator Using Functions

## Student Information

- **Name:** Stephen thompson
- **Campus:** New College Lanarkshire
- **Banner ID:** B01886612

## Project Description

This project involves creating a basic IP Address Validator using Python functions and string operations.

IP addresses are commonly used in cyber security logs and network monitoring. Before analysing an IP address, it is useful to check whether it follows the expected format.

The program uses a user-defined function called `validate_ip()` to check whether an entered IP address meets the basic IPv4 formatting requirements.

## Program Features

### 1. IP Address Input

- Asks the user to enter an IP address.
- Accepts the entered address as a string.
- Removes unnecessary surrounding spaces.

### 2. IP Address Validation

The `validate_ip()` function performs the following checks:

- Checks whether the IP address contains periods (dots).
- Checks whether the address contains exactly three dots.
- Checks whether the address contains four numerical groups (octets).
- Checks whether all four octets contain valid numbers.
- Checks whether each octet is between 0 and 255.
- Returns `True` if all basic validation requirements are met.
- Returns `False` if any validation requirement fails.

### 3. Validation Result

- Displays `Valid IP address` if the address passes validation.
- Displays `Invalid IP address` if the address fails validation.

## Example Inputs and Expected Outputs

### Example 1 – Valid IP Address

**Input:**

```text
192.168.1.10
```

**Output:**

```text
Valid IP address
```

### Example 2 – Invalid IP Address

**Input:**

```text
192.168.1.300
```

**Output:**

```text
Invalid IP address
```

### Example 3 – Missing Octet

**Input:**

```text
192.168.1
```

**Output:**

```text
Invalid IP address
```

### Example 4 – Non-Numeric Octet

**Input:**

```text
192.168.one.10
```

**Output:**

```text
Invalid IP address
```

## Python Concepts Used

- User-defined functions.
- Function parameters.
- Return values.
- String operations.
- String splitting.
- Conditional statements.
- Loops and iteration.
- Numeric conversion.
- Basic input validation.

## Technologies Used

- Python 3.
- Visual Studio Code.
- Git and GitHub.

## Project Files

- `ip_address_validator.py` – Main Python program.
- `README.md` – Project documentation.
- `LICENSE` – Repository licence.
- `screenshots/` – Testing screenshots.

## How to Run the Program

1. Open the GitHub repository.
2. Select the `ip-address-validator` branch.
3. Open the project in Visual Studio Code.
4. Open the `ip_address_validator.py` file.
5. Run the Python program.
6. Enter an IP address when prompted.
7. Review the validation result displayed in the terminal.

Alternatively, use the terminal:

```bash
python ip_address_validator.py
```

On some systems, use:

```bash
python3 ip_address_validator.py
```

## Testing and Evidence

The program should be tested using valid and invalid IP addresses.

Testing should include:

- A correctly formatted IP address.
- An IP address containing an octet greater than 255.
- An IP address containing fewer than four octets.
- An IP address containing more than four octets.
- An IP address containing letters.
- An IP address containing negative numbers.
- An IP address containing boundary values such as 0 and 255.
- An empty input.

Screenshots of the testing results will be saved in the `screenshots/` folder.

## GitHub Branch

- **Branch Name:** `ip-address-validator`
- **Task Number:** Task 3

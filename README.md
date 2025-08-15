# A Python tool that analyzes the strength of your password and checks if it has been exposed in past data breaches using the HaveIBeenPwned API.



# Features:

Checks if your password meets strong security criteria:
	At least 1 uppercase letter
	At least 1 lowercase letter
	At least 1 digit
	At least 1 special character
	Minimum 12 characters long
Provides feedback on how to strengthen weak passwords.
Verifies if your password has been found in past data breaches.
Keeps your password secure by never sending it in plain text.


# Clone the repository:
 git clone
Move to repo directory
 cd analyze_my_password
Run the tool
 python3 analyze_my_password


# How It Works:
Enter your password (input is hidden for security).
The tool checks if it meets the strength criteria:
	Uppercase letter
	Lowercase letter
	Digit
	Special character
	Minimum length of 12 characters

If weak: You get feedback on how to improve it.

If strong: The tool checks if it appears in the HaveIBeenPwned breach database.

You are told how many times (if any) your password has been found in breaches.

You can choose to check another password or exit.


# Security Note:

Your password is never sent to HaveIBeenPwned in plain text.
It is first hashed using SHA-1, and only the first 5 characters of the hash are sent for verification (following HIBP's k-anonymity model).

# PRODIGY_CS_03
Password Strength Checker
This repository contains a Python script that checks the strength of a password based on specific criteria. The script uses regular expressions to determine if the password contains uppercase letters, numeric characters, and special characters. Additionally, it checks the length of the password.

Features
Checks if the password contains at least one uppercase letter.
Checks if the password contains at least one numeric character.
Checks if the password contains at least one special character.
Checks if the password length is at least 8 characters.
Returns a strength score based on the criteria met.
Requirements
Python 3.x
re library (standard library, no need for installation)
Installation
Clone this repository to your local machine:
sh
Copy code
Navigate to the project directory:
sh
Copy code
cd password-strength-checker
Usage
To check the strength of a password, use the check_password function. The function takes a password string as input and returns a strength score.


# Example usage
password = input("Enter your password: ")
strength = check_password(password)
print(f"The strength of your password is: {strength}")
Strength Score
The strength score ranges from 0 to 4, with the following criteria:

+1 if the password contains at least one numeric character.
+1 if the password contains at least one uppercase letter.
+1 if the password contains at least one special character.
+1 if the password length is at least 8 characters.
File Structure
bash
Copy code
password-strength-checker/
│
├── password_checker.py   # Contains the password strength checking script
├── README.md             # This README file
└── requirements.txt      # (optional) List of dependencies
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

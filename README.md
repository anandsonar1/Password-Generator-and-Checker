# Password-Generator-and-Checker
This Python script allows users to check the strength of a password or generate a strong password. The script includes two main functions: check_p() for checking the strength of a user-provided password and generate_p() for generating a random strong password.


Features:

Password Strength Checker (check_p()):

Prompts the user to enter a password.
Evaluates the password based on length, inclusion of uppercase and lowercase letters, digits, and special characters.
Penalizes passwords that are purely alphabetical or numerical.
Reduces score if common patterns are found.
Categorizes the password strength as "Strong," "Medium," or "Weak."
Provides feedback if the password does not meet certain criteria.

Password Generator (generate_p()):

Randomly generates a password with a length between 8 and 12 characters.
Ensures the generated password includes at least one uppercase letter, one lowercase letter, one digit, and one special character.
Avoids common patterns to increase password strength.
Categorizes the generated password as "Strong," "Medium," or "Weak."

User Interface:

Provides a menu with three options: check a password, generate a password, and quit the program.
Continuously prompts the user until they choose to quit.

How to Use:
Run the script.
Choose an option from the menu:
Enter 1 to check the strength of a password.
Enter 2 to generate a strong password.
Enter 3 to quit the program.
Follow the prompts to either enter a password for checking or view the generated password and its strength score.

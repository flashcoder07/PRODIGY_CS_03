import re

def check_password(password):
    uppercase = re.compile(r'[A-Z]')
    numeric = re.compile(r'\d')
    special = re.compile(r'[!@#$%^&*()\-_=+{};:,<.>/?]')

    check_uppercase = bool(uppercase.search(password))
    check_numeric = bool(numeric.search(password))
    check_special = bool(special.search(password))

    score = 0
    if check_numeric == True:
        score += 1
    if check_uppercase:
        score += 1
    if check_special:
        score += 1
    if len(password) >= 8:
        score += 1

    return score

password = input("Enter your password: ")
strength = check_password(password)
print(f"The strength of your password is: {strength}")

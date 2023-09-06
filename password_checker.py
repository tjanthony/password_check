import re

def strong_password(password):

    if len(password) < 8:
        return False
    
    if not any (char.isdigit() for char in password):
        return False
    
    if not any (char.isupper() for char in password):
        return False

    if not any (char.islower() for char in password):
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

password = input("Enter Password::")

if strong_password(password):
    print("Strong Password")
else:
    print("Weak Password")        
import random
import string

def password_generator(password_length):
    '''
    (None) -> str
    '''
    
    password= ''
    
    gen = random.choice(string.hexdigits)
    
    for i in range(password_length):
        gen = str(random.choice(string.hexdigits)) 
        password += gen
    
    return password

while True:
    try:
        
        password_length = int(input("Enter the length of the password you would like: "))
        
        if password_length <= 0:
            raise ValueError("Password length cannot be less than or equal to 0.")
        
        break

    except (TypeError, ValueError):
        print("That is not a valid password length.")

print("Key generated:", password_generator(password_length))

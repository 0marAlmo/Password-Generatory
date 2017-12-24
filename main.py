import random
import string

def password_generator(password_length):
    '''
    (None) -> str
    '''
    
    gen = random.choice(string.hexdigits)
    
    password= ''
    
    for i in range(password_length):
        
        gen = str(random.choice(string.hexdigits)) 
        
        password += gen
    
    return password

def get_password_length():

    while True:
    
        try:
        
            password_length = int(input("Enter the length of the password you would like: "))
        
            if password_length <= 0:
                raise ValueError("Password length cannot be less than or equal to 0.")
        
            break

        except (TypeError, ValueError):
            print("That is not a valid password length.")
    
    return password_length

while True:
    
    password_length = get_password_length()
    
    print("Password generated:", password_generator(password_length))

    repeat = input("Would you like to generate another password? (y/n): ")
    
    if repeat.lower() != "yes" and repeat.lower() != "y":
        print("Thank you for using this password generator!")
        break


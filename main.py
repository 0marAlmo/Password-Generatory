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

password_length = int(input("Enter the length of the password you would like: "))

print("Key generated:", password_generator(password_length))

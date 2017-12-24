import random
import string

def password_generator(password_length):
    '''
    (None) -> str
    '''
    
    gen = random.choice(string.hexdigits)
    repeat= input("Would you like to generate a password? (yes or no) ")

    while repeat.strip().lower() == 'yes':
        password= ''
        for i in range(password_length):
            gen = str(random.choice(string.hexdigits)) 
            password += gen
        print(password)

        repeat= input("Would you like to generate a password? ")


password_length = int(input("Enter the length of the password you would like: "))
    
print("Key generated:", password_generator(password_length))

import random
import string 


key_length= int(input("Enter the length of the password you would like: "))
    
def password_generator():
    password= ''
    gen= (random.choices(string.hexdigits))
    for i in range(key_length):
        gen= str(random.choices(string.hexdigits)) 
        password+=gen
        FinPass=str(''.join(password))
    return "Key generated: " + FinPass

print(password_generator())

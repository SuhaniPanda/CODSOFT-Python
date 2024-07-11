#Password Generator
'''
User Input: Prompt the user to specify the desired length of the password.
Generate Password: Use a combination of random characters to generate a password.
Display the Password: Print the generated password on the screen.
'''
import random,string
l=int(input("Enter Length of Password: "))
c= string.ascii_letters + string.digits + '!@#$%^&*()'
for i in range(l):
    print(random.choice(c),end='')

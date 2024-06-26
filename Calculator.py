#Design a simple calculator with basic arithmetic operations
#Prompt the user to input two numbers and an operation choice.
a=int(input("Enter Number: "))
b=int(input("Enter Number: "))
c=input("Enter operator: ")

if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='%':
    print(a%b)
else:
    print("Unknown symbol entered")

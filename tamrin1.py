import random

name = input("Enter the name :").lower()
age = input("Enter the age :")
color = input("Enter the Favorite color :").upper()
symbol= "@#$%&*"
s= list(name)+ list(age)+ list(color)+ list(symbol)
random.shuffle(s)
r = "".join(s[ :12])
print("Secure Password:" ,(r))

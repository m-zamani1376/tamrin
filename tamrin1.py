import random
while True:
    try:
        while True:
            name = input("Enter the name :").lower().strip()
            if name :
                break
            else:
                print("Please Enter the name")
        while True:
            age = input("Enter the age :").strip()
            if age:
                break
            else:
                print("Please Enter the age")
        while True:
            color = input("Enter the Favorite color :").upper().strip()
            if color:
                break
            else:
                print("Please Enter the color")
        symbol= "@#$%&*"
        s= list(name)+ list(age)+ list(color)+ list(symbol)
        random.shuffle(s)
        r = "".join(s[ :12])
        print("Secure Password:" ,(r))
    except ValueError:
        print("Please Enter the character")

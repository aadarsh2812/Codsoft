def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def div(x,y):
    return x/y
y=True
choice = y
while choice:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("""
addition - 1
subtraction - 2
multiply - 3
division - 4
""")
    opp=int(input("enter your choice:"))
    if opp == 1 :
        print(add(num1,num2))

    elif opp == 2:
        print(sub(num1,num2))

    elif opp == 3:
        print(multiply(num1,num2))

    elif opp == 4:
        print(div(num1,num2))

    else :
        print("please enter a valid input")

    choice = input("if you want to contiunue type 'y' or else type 'N': ")
    if choice=='n' or choice=='N':
        choice=False

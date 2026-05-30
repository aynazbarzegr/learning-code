def sum(a,b):
    return a+b
def tafrigh(a,b):
    return a-b
def zarb(a,b):
    return a*b
def tagsim(a,b):
    return a/b 
while True:
    choice = input("enter your opration +,-,*,/:")
    number1= int(input(" enter number1:")) 
    number2= int(input("enter number2:"))
    if choice == "+":
        print(sum(number1,number2))
    elif choice == "-":
        print(tafrigh(number1,number2))
    elif choice == "*":
        print(zarb(number1,number2))
    elif choice == "/":
        print(tagsim(number1,number2))
    else:
        print("incurrect operation")
            

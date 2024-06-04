# Calculator
'''Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multipy(x,y):
    return x*y

def divide(x,y):
    return x/y
    

print("SIMPLE CALCULATOR")
print("You can perform the following operations- \n 1.Add(+) \n 2.Subtract(-) \n 3.Multiply(*) \n 4.Divide(/) \n 5.Exit \n")

while(True):
    choice=input("Enter your choice: ")
    
    if choice=='5':
        break
    
    operand1=float(input("Enter first number: "))
    operand2=float(input("Enter second number: "))

    choice=choice.lower()

    match choice:
        case '1'|'add'|'+':
            result=add(operand1,operand2)
            print(f"{operand1} + {operand2} = {result}")
            print("\n")
        case '2'|'subtract'|'-': 
            result=subtract(operand1,operand2)
            print(f"{operand1} - {operand2} = {result}")
            print("\n")
        case '3'|'multiply'|'*':
            result=multipy(operand1,operand2)
            print(f"{operand1} X {operand2} = {result}")
            print("\n")
            
        case '4'|'divide'|'/':
            result=divide(operand1,operand2)
            print(f"{operand1} / {operand2} = {result}")
            print("\n")
        
        case _:
            print("Invalid choice")
            print("\n")
            
                    
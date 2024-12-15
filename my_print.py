def PRINT(name:str) :
    print(f"Asalam-o-Alikum , {name} ! ")
    
def PRINT_RETURN(name: str) -> str :
        print(f"Asalam-o-Alikum , {name} !")
        
        return f"Hello {name} !"
    
    
    
    
def simple_calculator(): 
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print(f"The result is: {num1 + num2}")
    elif operation == '-':
        print(f"The result is: {num1 - num2}")
    elif operation == '*':
        print(f"The result is: {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation")

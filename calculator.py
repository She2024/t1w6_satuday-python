# simple calculatort using if-else statements

# Get user inputs
num1 = float(input("Enter first number: "))
operation = input("Enater oeration (+,-,*,/):")
num2 = float(input("Enter second number: "))

#Perfom calculation using if-else
if operation =="+":
    result = num1 + num2
elif operation =="-":
    result = num1 - num2
elif operation =="*":
    result = num1 * num2
elif operation =="/":
    result = num1 / num2  
        if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by Zero"
else: 
    result = "Error! Invaild operation"

print(f"The result is: {result}")    
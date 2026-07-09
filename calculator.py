num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Select operation (1/2/3/4): ")
print("1. Add")
print("2. subtract")
print("3. Multiply")
print("4. Divide")

# perform calculation
if operation == '1':
    print(num1, "+", num2, "=", num1 + num2)
    print("Result: ", num1 + num2)
elif operation == '2':
    print(num1, "-", num2, "=", num1 - num2)
    print("Result: ", num1 - num2)
elif operation == '3':
    print(num1, "*", num2, "=", num1 * num2)
    print("Result: ", num1 * num2)
elif operation == '4':
    print(num1, "/", num2, "=", num1 / num2)
    print("Result: ", num1 / num2)

else:
    print("Invalid operation")
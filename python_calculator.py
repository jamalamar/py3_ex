
#Wrapping input in a float to only take numbers
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter the second number: "))


if op == "+":
	print(num1 + num2)
elif op == "-":
	print(num1 - num2)
elif op == "*":
	print(num1 * num2)
elif op == "/":
	print(num1 / num2)
else:
	print("Invalid operator")



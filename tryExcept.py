
#Always expect specific error for best practice

try:
	number = int(input("Enter a number: "))
	print(number)

except ZeroDivisionError as err: 	#Created an exception for this specific error.
	print(err)

except ValueError:			#Created an exception for this specific error.
	print("Invalid Input")
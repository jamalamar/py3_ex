
#Function to raise a Base number to a Power:

def raise_to_power(base_num, power_num):
	result = 1						#Variable to store result.

	for index in range(power_num):	#This function will loop as many times as the power_num.
		result = result * base_num	#Every loop, the result will be multiplied by the base number and updated.
	return result					#Once loop ends it will return the final result.


print(raise_to_power(2, 10))
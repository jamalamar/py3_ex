
#Simple While-Loop
i = 1

while i <= 100:
 	print(i)
 	#Short hand for: i = i + 1
 	i += 1

#Once loop is finished print this:
print("Done with While-Loop")

#########################################

#Simple For-Loop
for letter in "This is a String":
	print(letter)

print("Done with For-Loop")


#########################################

#For-Loop with Arrays
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
	print(friend)

#Same result
for index in range(len(friends)):
	print(friends[index])

#########################################


#For-Loop with numbers
for index in range(25):
	print(index)

for index in range(5, 10):
	print(index)


#########################################




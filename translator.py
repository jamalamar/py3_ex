
#Change all vowels to letter "E"

def translate(phrase):
	translation = ""

	for letter in phrase:
		if letter in "AEIOUaeiou":
			translation = translation + "e"
		else:
			translation = translation + letter
	return translation


print(translate("Hello my name is jamal"))
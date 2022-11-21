def i2eye(text):
	newText1 = text.replace("i", "eye")
	newText2 = newText1.replace("I", "Eye")
	return newText2

  

if __name__ == "__main__":
	text = input("Enter some text: ")
	print(i2eye(text))

def shout(word):
	shouted_words = f"{word.upper()}, {word.upper()}, {word.upper()}!"
	return shouted_words

  
if __name__ == "__main__":
	word = input("Enter your favourite word: ")
	print("That's a great word!!")
	print(shout(word))

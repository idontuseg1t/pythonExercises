''' I'm using the index method anyway even if the hint says not to '''

def theFinder(text):
	findthe = f"The first`qsqwwwdddeef the is at {text.index('the')}"
	return findthe

if __name__ == "__main__":
	txt = input("Enter some text: ")
	try:
		print(theFinder(txt))
	except:
		print("There is no 'the' in that string") # Extension component

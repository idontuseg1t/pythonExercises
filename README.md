# Python Exercises

# 1 Basic “Input, Process, Output” Programs

In these exercises we use the input function to get data and print to print out results. The code just runs from top to bottom (in sequence). Note - this booklet is not stand-alone - it is intended to be used with a sequence of lessons introducing the various concepts.

## 1.1 Input and Output — Strings

### Instructions

Create a program that will prompt the user for their First and Last name, then output the classic James Bond response


```python
# Input names  
first_name = input("First name: ")  
Last_name = input("Last name: ")  
# Process names to produce output (optional)  
  
# Print output  
print("The name's " + first_name + “ ” +  last_name)
# OR
print(f"The name's {first_name} {last_name}")
```


## 1.2 Input and Output — Integers

### Instructions

Create a program that will prompt the user for their age, then output their age in dog years.

```python
# Input age  
age = int(input("Enter your age in years: "))  # the int() function converts the input to an int  
  

# Process

# dog_age = age * 7*    # FIX THIS

  
# Output dog age

print(f"Your age in dog years is {age * 7} ")       # FIX THIS
```

## 1.3 Input and Output — Floating Point Numbers

### Instructions

Create a program that will prompt the user for the current temperature in degrees Celsius and output the corresponding temperature in degrees Fahrenheit rounded to one decimal place

```python
# input

temp_C = float(input("Enter degrees in celsius: ")) 
# the float() converts the input to a number

# Process

temp_F = (temp_C * 1.8) + 32

# Output

# Hint: Rounding

print(f"The temperature in farenheit is {round(temp_F,1)}")
```

## 1.4 Body Mass Index — version 1

### Instructions

Create a program that will prompt the user for their height and mass and then output their BMI to 1 decimal place

```python
height = float(input("Enter your height in m: "))

mass = float(input("Enter your mass in kg: "))

  

print(f"Your BMI is {round(mass/(height**2),1)}")
```

## 1.5 Simple Interest — version 1

### Instructions

Create a program that will prompt the user for their Principal amount in dollars (this is the original deposit), the interest rate as a percentage. Your program will then calculate and print:

1.  the interest earned in a year

2.  The amount of money the user has in the bank at the end of 7 years


All output values should be rounded to the nearest cent and displayed two two decimal places

```python
principalInput = float(input("Enter your principal amount in dollars: "))
interestInput = float(input("Enter the interest rate as a percentage: "))
  

interestPerYear = principalInput * (interestInput/100)
amountAfterYear = principalInput + (7 * interestPerYear)

print(f"You will earn ${interestPerYear:.2f} interest per year")
print(f"After 7 years you will have ${amountAfterYear:.2f}")
```

# 2 Functions

Functions are named pieces of reusable code that help you structure understandable, testable, and maintainable programs. You have used built-in functions before, such as print, input and round; and will soon see ones like min, max, len, and range. These all take input data and either return a value or have a side effect like displaying something on the screen.

  

Examples that you have seen:

-   print(arg1, arg2, …) takes zero or more arguments and prints them all to the screen separated by a single space and terminated by a new line (by default). It does not return any value (to be precise, it returns the value None).
-   input(prompt) takes a single argument that is displayed to prompt the user and returns a string containing the user’s response.
-   round(value) will take a floating point number and return the closest integer. 

You can define your own functions using the def keyword. For example here is a function that will eat a number and spit out its square; and one that will give the value of an account given its principal compounding annually with a nominal interest rate and the number of years compounding

```python
def square(num):  
  sq_num = num * num  
  return sq_num
```

```python
def future_value(principal, nom_rate, years):  
  factor = (1 + nom_rate/100)**years  
  return factor * principal
```

You can optionally add Type Hints to functions to make the types of input and output clearer, e.g.,

```python
def square(num: float) -> float:  #Define the function
  sq_num = num * num  
  return sq_num  
print(square(2), ", ", square(3.0))  # Call the function
```

Type hints in Python help humans read the code and allow the IDE to help find errors before you run your code. However, in most instances they do not change how the code runs.

Some terminology: Arguments and Parameters. In the definition of a function the inputs are called parameters. When the function is called, the values passed through as inputs are called the arguments. However, these terms are often used interchangeably.  [[stackoverflow.com/a/156778](https://stackoverflow.com/a/156778)]  
In the example above: num is the parameter; and 2 and 3.0 are the arguments when the function square was called.   
Python can have positional arguments (like above), named arguments and default values. We will learn about the latter two later!


Some more terminology: Function vs Procedure vs Subroutine vs Method. Loosely speaking:

-   A subroutine is any callable bit of code that will run and then return the execution back to the point in the original code from which it was called. This is old terminology.
-   A function is a callable bit of code that can take arguments and returns a value
-   A procedure is (usually) a function that does not return a value, usually it has side effects like printing to the screen.
-   A method is a function that is called on an object. We will see built-in methods like str.upper() and list.sort() soon. We will learn more about Object Oriented Programming later!

## 2.1 Twice cubed

### Instructions

Create a function that will take a number, multiply it by two and then cube it. 

```python
def twice_then_cubed(num):  
  result = (2*num)**3
  return result  
  
print(twice_then_cubed(2)) # Note: "True" parameter is equal to 1
```

# 3 String Operations and Methods

## 3.1 Length of a string

### Instructions

Create a program that will prompt the user for a word, then it will tell them how many characters are in the word (including spaces, punctuation, etc...)

```python
userString = input("Type something: ")
print(f"The length of that string is {len(userString)}")
```

## 3.2 Shout a string

### Instructions

Create a program that will prompt the user for a word, then "SHOUT" it back to them three times. The code that produces the string printed in the last line should be wrapped in a function called shout.

```python
def shout(word):
	shouted_words = f"{word.upper()}, {word.upper()}, {word.upper()}!"
	return shouted_words

  
if __name__ == "__main__":
	word = input("Enter your favourite word: ")
	print("That's a great word!!")
	print(shout(word))
```

## 3.3 Eye Spy

### Instructions

Create a program that will prompt the user for some text and return it with every lowercase "i" replaced with "eye" and every uppercase "I" with "Eye".

```python
def i2eye(text):
	newText1 = text.replace("i", "eye")
	newText2 = newText1.replace("I", "Eye")
	return newText2

  

if __name__ == "__main__":
	text = input("Enter some text: ")
	print(i2eye(text))
```

## 3.4 Find the "the"

### Instructions

Create a program that will prompt the user for some text and will output the position of the first occurrence of "the" in the text.  
Extension: Detect when there is no “the” and print an appropriate message.

```python

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
```

## 3.5 First, Blank, Last

### Instructions

Create a function that will take a word and replace all of the inside letters with underscore characters. Use that function to create the following

```python

```

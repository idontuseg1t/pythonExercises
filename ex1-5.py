principalInput = float(input("Enter your principal amount in dollars: "))
interestInput = float(input("Enter the interest rate as a percentage: "))
  

interestPerYear = principalInput * (interestInput/100)
amountAfterYear = principalInput + (7 * interestPerYear)

print(f"You will earn ${interestPerYear:.2f} interest per year")
print(f"After 7 years you will have ${amountAfterYear:.2f}")

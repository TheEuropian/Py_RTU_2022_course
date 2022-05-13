print("1.st exercise")
temp = float(input("Please type you body temperature here: "))
if temp < 35:
    print("Are you cold?")
elif temp >= 35 and temp <= 37:
    print("All good. You are fine.")
else:
    print("You have a fever.")
    
print("2.nd exercise")
salary = float(input("Please enter your salary here: "))
w_years = float(input("How many years do you work for us? Please enter here: "))
if w_years >= 2:
    bonus = salary * .15 * (w_years -2)
    print("Your Christmas bonus is: ",bonus)
else: print("Sorry, but you work less than two years")

print("3.rd exercise")
num1 = float(input("Please enter 1st number here: "))
num2 = float(input("Please enter 2nd number here: "))
num3 = float(input("Please enter 3rd number here: "))
if num1 < num2 < num3:
    print(num1, num2, num3)
elif num1 < num2 > num3:
    print(num1, num3, num2)
elif num2 < num1 < num3:
    print(num2, num1, num3)
elif num2 < num1 > num3:
    print(num2, num3, num1)
elif num3 < num1 < num2:
    print(num3, num1, num2)
elif num3 < num1 > num2:
    print(num3, num2, num1)
else: print("Try again - We don't play with equal numbers.")
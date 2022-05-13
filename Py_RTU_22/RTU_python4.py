print("1.st exercise\n")

num = int(input("Please enter the number to iterate to: \n"))
i = 1
while i <= num:
    if i%7==0 and i %5==0:
        print("FizzBuzz",end="\n")
        i+=1    
    elif i%5==0:
        print("Fizz", end="\n")
        i+=1   
    elif i%7==0:
        print("Buzz", end = "\n")
        i+=1    

    else:
        print(i, end="\n")
        i+=1
        
print("\n2.st exercise\n")

num = int(input("Please enter the height of the Christmas Tree: \n"))
spaces = num - 1
stars = 1
for i in range(num):
    print(" "*spaces, "*"*stars)
    spaces -=1
    stars += 2
    
print("\n3.st exercise\n")

number = int(input("Please enter the number to check: \n"))

flag = False
for i in range(2, number):
    if number%i == 0:
        flag = True
        break
if flag == True:
    print("Not a prime number")
else:
    print("Prime number")
    






print("1st exercise")
print("a.")
num1 = float(input("Please eneter the number: "))
num2 = float(input("Please eneter the number: "))
average = (num1 + num2)/2
print(average)
print("1st exercise")
print("c.")
myList=[]
while True:
    myInput = input("Please type your number or q to exit the game.")
    if myInput == "q":
        break
    myInput = float(myInput)
    myList.append(myInput)
    
    if len(myList) <=5:
        print("you need to add more numbers.")
        
    if len(myList) >5:
        myList = sorted(myList)
        print(f"The greatest numbers you added are {myList[-3:]} and smallest are {myList[:3]}")
        print(f"The average of your max num and min num is {(max(myList) + min(myList)) / 2}")
        print(f"You have added {len(myList)} numbers and the average of the list is {sum(myList)/len(myList)}")


print("2nd exercise")
num1 = int(input("Please eneter the 1st number: "))
num2 = int(input("Please eneter the 2nd number: "))
myList=[]
if num1 <= num2:
    smallNum = num1
    bigNum=num2
else:
    smallNum = num2
    bigNum=num1
while smallNum!=bigNum+1:
    cube= smallNum**3
    print(f"{smallNum} in {cube}")
    myList.append(cube)
    smallNum+=1
print(myList)
print("3rd exercise")
print("Lai būtu interesantāk, tad apgriezu otrādi arī teikumu.")
text = input(print("Please enter your text: "))
reverseWords= text.split()
reverseWords.reverse()
newText=""
for word in reverseWords:

    for letters in word[::-1]:
        newText+=letters
    newText+=" "
print(newText)
print("1st exercise")
name = input(print("Please type your name here:"))
newName = name[::-1].capitalize()
print(f"{newName}, pamatigs juceklis vai ne {name[0]}?")

print("2nd exercise")
theRules = "To quite the task please type: q"
print(theRules)
text2check = input(print("Please enter the text to hide:"))
hidenName = " "
gues = " "
while gues != "q":
    gues = input(print("Please type your gues here:"))
    for letter in text2check:
        if gues == letter:
            hidenName += gues
        elif letter == " ":
            hidenName += "_"
        elif gues != letter:
             hidenName += "*"
    print(hidenName,end="\n")
    hidenName = ""
print("3rd exercise")
text = input("Ievadi tekstu: ")
newText = text.replace("nav slikts", "ir labs")
print(newText)
inputText = input("Input a new text here: ")
word1= "not"
word2="good"
word3 = "excelent"
textFind= inputText.find(word1)
textFind2 = inputText.rfind(word2) + len(word2)
positiveText = inputText[:textFind] + word3 + inputText[textFind2:]
if textFind != inputText[-1] and textFind2 != inputText[-1]:
    print(positiveText)
else: print("The text doesn't meet all necessary conditions.")


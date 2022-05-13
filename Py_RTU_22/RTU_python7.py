print("1st exercise")
def addMult(a,b,c):
    if a>b and a>c:
        res=(c+b)*a
        print(res)
    elif b>a and b>c:
        res=(a+c)*b
        print(res)
    elif c>a and b<c:
        res=(a+b)*c
        print(res)
    else: print("We do not play with equal numbers")
addMult(3,7,8)

print("2nd exercise")
text = input("Input your text:\n")
text2 = text[::-1]
revText = "".join(text2.split())
text="".join(text.split())
def checkPalidrome():
    if text == revText:
        return True
    else: return False
print(checkPalidrome())
print("3rd exercise")
pO = float(input(print("Input the number of residents in your city:")))
percP = input(print("Residents increase in every year in %:"))
perc = (float(pO) * (float(percP) / 100))
delta = float(input(print("population decrease and growth ratio:")))
p = float(input(print("Population target:")))
years = 0
def Cpopulation(pO,perc,delta):
    years = 0
    while pO<p:
        pO = float(pO) + perc + delta
        years +=1
        if delta <= 0:
            return print("-1")
            break
    return years

print(Cpopulation(pO,perc,delta))  


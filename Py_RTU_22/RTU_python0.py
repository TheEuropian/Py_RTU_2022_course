from random import randrange


def func(n):
    mydict = {}
    total = 0
    i=0
    x=1
    for i in range(n):
        mydict['key'+str(i)] = total
        total = 0
        for x in range(7):
            total += randrange(1,7)
    
    return mydict
print(func(12))










from collections import Counter
from random import randrange



def func(n):
    total = 0
    i=0
    x=1
    mydict={}
    for i in range(n):
        for x in range(7):
            total += randrange(1,6)
        mydict['key'+str(i)] = total
        total = 0
        func.mydict = mydict
    func.total_list= list(mydict.values())   
    
    return func.total_list
print(func(100000))
most_res = Counter(func.total_list)
print(most_res)


import matplotlib.pyplot as plt

plt.bar(most_res.keys(),most_res.values())
plt.show()









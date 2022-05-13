from pickle import NONE
from mod_count_numbers import count_numbers as cn
my_list = [92,5,8,60,15,26,10]
cn(my_list)

#The example above is just for me. To check if I understand the subject.

print("Exercise 1")
x=input("Enter the number you want to try with factorial function:  ")
x=int(x)
import math
from math import factorial as Mfact
print(Mfact(x))
print("Exercise 1.b")
from math import prod as Mprod
list1=[2,3]
list2=[5,10,2]
def sum_prod(list1,list2):
    return Mprod(list1)+Mprod(list2)  
print(sum_prod(list1,list2))

print("Try with multiple lists of int numbers.")
n=int(input("Enter the number of lists are you going to create: "))
m_lists = []

for i in range(n):
    i_list=[]
    l_num = NONE
    print("To close the list type q")
    while l_num != "q":
        l_num=input("Enter your number: ") 
        if l_num != "q":
            l_num=int(l_num)
            i_list.append(l_num)
    i=i+1
    m_lists.append(i_list)

def m_lists_total(m_lists):
    total_of_list = 0
    for m_list in m_lists:
        total_of_list += Mprod(m_list)
    print(total_of_list)
    return total_of_list
print(m_lists)
m_lists_total(m_lists)



    












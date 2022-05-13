big_list = []
new_list= []
new_num = 0
answer = input("Type yes if you want to create a new list.  ")
try: 
    while answer == "yes":
        new_num= int(input("Enter a new number "))
        if new_num== "q":
            big_list.append(new_list)
            break
        else:
            new_list.append(new_num)
except: print(big_list, new_list)       
  

def count_multipl_num(big_list):
    big_list.append(list2)
    return big_list
print(count_multipl_num(big_list))


if __name__ == "__main__":
  print('Inside module')
  #count_multipl_num(big_list)
if __name__ != "__main__":
  print("Exported module")


try:
    my_list = []
     
    while True:
        my_list.append(int(input()))
         
# if the input is not-integer, just print the list
except:
    print(my_list)
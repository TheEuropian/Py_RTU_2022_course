def count_numbers(my_list):
      total = 0
      average = 0
      my_num = 0
            
      for number in my_list:
        if number >0 :
          total+= number
          average = total / len(my_list)
          average = round(average,2)
          my_num +=1

  
      return print(f"{total=}, {average=}, {my_num=}")
my_list=[]

if __name__ == "__main__":
  print('Inside action just for checking the module')
  count_numbers(my_list)
if __name__ != "__main__":
  print("I finaly got the idea how it works.")
#exercise 1
def get_min_avg_max(numbers):
   
    minN = min(numbers)
    maxN = max(numbers)
    aveN = sum(numbers) / len(numbers)
  
    answer = (minN,maxN,aveN)
    
    return print(f"The answer is {answer}.")
numbers = [1,5,86,41]
get_min_avg_max(numbers)

#exercise 2
def get_common_elements(seq1,seq2,seq3):
    seq1 = set(seq1)
    seq2 = set(seq2)
    seq3 = set(seq3)
    letters = [i for i in seq1 if i and i in seq2 and i in seq3]
    letters = tuple(letters)
    print(letters)
    

get_common_elements("abce",['a','b','e'],('b','c','e'))
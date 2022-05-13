print("1st exercise")
def get_char_count(text):
    newDictionary = {}
    for letter in text:
        if letter not in newDictionary:
            newDictionary[letter.lower()] = 1
        else:
          newDictionary[letter.lower()] += 1
    return newDictionary
print(get_char_count("Izteikts ieteikums: saskaiti visus i"))

print("2nd exercise")
d = {'a':5, 'b':6, 'c':5, 'd':13, 'e': 5}
bad_val = 5
good_val = 10
newD = {}
def replace_dict_value(d, bad_val, good_val):
    for k, v in d.items():
        if v == bad_val:
            newD[k] = good_val
        else:
            newD[k] = v
    return newD
print(replace_dict_value(d, bad_val, good_val))


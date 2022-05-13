with open("veidenbaums.txt", encoding="UTF-8") as f:
   my_text=f.readlines()

def file_line_len(my_text):
    totlal_lines = 0
    for line in my_text:
        totlal_lines+=1
    return print(totlal_lines)
file_line_len(my_text)



new_veidenbaum_text = []
def get_poem_lines(my_text):
    for i in my_text:
        if not i.strip() or ("***") in i:
             continue
        if i:
           new_veidenbaum_text.append(i)
    return new_veidenbaum_text
get_poem_lines(my_text)

with open('veidenbaums.txt',encoding="UTF-8") as new_v_text:
    filtered_text=[]
    for i in new_v_text:
        if not i.strip() or ("***") in i:
             continue
        if i:
           filtered_text.append(i)


with open('new_text_veidenbaums.txt', mode='w',encoding="UTF-8") as f:
    f.writelines(filtered_text)


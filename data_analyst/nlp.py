txt ='''
Python is one of the most promising programming languages today. 
Due to the smplicity of Python syntax, many researchers and scientists prefer
Python over many other languages
'''

txt = txt.replace('.', '').replace(',','')
lst = txt.split()
print(lst)

dct = {}
for w in lst:
    c = dct.setdefault(w,0)
    dct[w] +=1

#print(dct)

dct_sorted = dict(sorted(dct.items(), key = lambda x: x[1], reverse= True))
print(dct_sorted)

my_list = [1, 2, 2, 3, 4, 4, 5]

# Using list comprehension to remove duplicates
unique_list = [item for index, item in enumerate(my_list) if item not in my_list[:index]]

print(unique_list)  # Output: [1, 2, 3, 4, 5]

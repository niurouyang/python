nested_list = [[1, 2], [3, 4], [5, 6]]

# Use a list comprehension to unpack the nested lists
flat_list = [x for sublist in nested_list for x in sublist] 
print(flat_list)
# this chapter introduce how to combine list, set, tuble, dictionary together
# to combine list and tuble together use +
# to combine dictionary togther use **dict1 + **dict2


'''orders_detail = []
for o in orders:
    for d in details:
        if d[0] == o[0]:
            orders_detail.append(o+d[1:])'''            
# replace above code with one line code as below

# order_details_1 = [[o for o in orders if d[0]==o[0]][0] + d[1:] for d in details]

# order_details_2 = [[o for o in orders if d[0] in o][0] + d[1:] for d in details if d[0] in [o[0] for o in orders]]
# this code to prevent there is difference between orders and details list.

# order_details_right = [[o for o in orders if d[0] in o][0] + d[1:] if d[0] in [o[0] for o in orders] else (d[0],None,None) +d[1:] for d in details
# This is a right join, returns all rows from the right dataset and only the matched rows from the left dataset.
# Here, you add an else clause to the if clause assigned to the for d in 'details' loop. This else clause works for any 'details' row that doesn't 
# have a matching row in 'orders'. It creates a new tuple containing the order number plus two None entries to take the place of the missing 'orders' 
# fields, and it concatenates that tuple with the row from 'details', yielding a row with the same structure as all the others. So the generated 
# dataset will include the 'details' row that doesn't have a matched row in 'orders' in addition to all the matching rows.

# sum(pr*qt for -,-,-,-,-,pr,qt in orders_details_right)
# sum the price  * quantity in orders_details_right dataset

# sum(pr*qt for _,dt_,_,_,pr,qt in orders_details_right if dt !=None)
# Filter the the 'None' in date field.
# 
#  
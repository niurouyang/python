import numpy as np
jeff_salary = [200,300,400]
nick_salary = [400,300,200]
tom_salary = [250,250,250]
base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])
# The extra [] in ([jeff_salary, nick_salary, tom_salary]) will change the dimension of the array

maya_salary = [350,350,350]
john_salary = [275,275,275]
base_salary2 = np.array([maya_salary,john_salary])

base_salary = np.concatenate((base_salary1,base_salary2), axis=0)

new_month_salary = np.array([[300],[250],[200],[240],[260]])

base_salary= np.concatenate((base_salary, new_month_salary), axis=1)
# axis 0 means add to row, axis 1 add to column

next_two_month_salary = np.array([[300,250],[400,350],[500,450],[400,350],[300,250]])
base_salary = np.concatenate((base_salary,next_two_month_salary), axis=1)

leo_salary = [[220,230,240,250,260,270]]

# here again, the dimension has to be change
base_salary= np.append(base_salary,leo_salary,axis=0)
print(base_salary)
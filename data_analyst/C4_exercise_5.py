# object: read a json file and print it to the format as required. 
import pandas as pd
import json

with open('python/data_analyst/data.json', 'r') as file:
    json_data = json.load(file)
#with open('python/data_analyst/data.csv','a') as csv_file:

for key,value in json_data.items():
    for index, item in enumerate(value):
        for key1,value1 in item.items():
            print(f"{key1} : {value1}")
        if index != len(value) -1 :
            print("\n")

''' use pandas dataframe to solve the problem
df = pd.DataFrame(json_data)
for index, row in df.rows: # we should not use iterrows,instead we should use rows
    #print(index)
    for row_detail in row:
        for key,value in row_detail.items():
            print(f"{key}  : {value}")
    if index != df.index.max():
        print("\n")
'''
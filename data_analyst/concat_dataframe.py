# example how to combine dataframe together

# 1. use concat
import pandas as pd

jeff_salary = [200,300,400]
nick_salary = [400,300,200]
tom_salary = [250,250,250]
maya_salary = [350,350,350]
john_salary = [275,275,275]

salary_df1 = pd.DataFrame(
    {'jeff': jeff_salary,
     'nick': nick_salary,
     'tom' : tom_salary}
)
salary_df1.index=['June','July','August']
salary_df1 = salary_df1.T
# T is a shorthand for the dataframe.transpose() method, it will change the index to employee's name

salary_df2 =  pd.DataFrame(
    {'maya': maya_salary,
     'john': john_salary},
    index=['June','July','August']
).T

salary_df = pd.concat([salary_df1,salary_df2])

# example to concatenation along Axis =1
salary_df3 = pd.DataFrame(
    {'September':[230,240,250,260,270],
     'October': [350,340,330,320,310]
     },
    index=['jeff','nick','tom','maya','john']
)
salary_df = pd.concat([salary_df,salary_df3], axis=1)

#remove columns/rows from a Dataframe
salary_df = salary_df.drop(['September','October'], axis=1)
salary_df = salary_df.drop(['nick','maya'],axis=0)

# Concatenating Dataframes with a Hierachical Index
df_date_region1 = pd.DataFrame(
    [
        ('2022-02-04','East',97),
        ('2022-02-04','West',243),
        ('2022-02-05','East',160),
        ('2022-02-05','West',35),
        ('2022-02-06','East',110),
        ('2022-02-06','West',86),
    ],
columns=['Date','Region','Total']).set_index(['Date','Region'])

df_date_region2 = pd.DataFrame(
    [
        ('2022-02-04','South',114),
        ('2022-02-05','South',325),
        ('2022-02-06','South',212),
    ],
columns=['Date','Region','Total']).set_index(['Date','Region'])

df_date_region = pd.concat([df_date_region1,df_date_region2]).sort_index(level=['Date','Region'])
# without sort_index(), the result will like 
#                    Total
#Date       Region       
#2022-02-04 East       97
#           West      243
#2022-02-05 East      160
#           West       35
#2022-02-06 East      110
#           West       86
#2022-02-04 South     114
#2022-02-05 South     325
#2022-02-06 South     212

# 2. implementing a right join by using merge

orders = [
 (9423517, '2021-08-04', 9001),
 (4626232, '2021-08-04', 9003),
 (9423534, '2021-08-04', 9001),
 (9423679, '2021-08-05', 9002),
 (4626377, '2021-08-05', 9003),
 (4626412, '2021-08-05', 9004),
 (9423783, '2021-08-06', 9002),
 (4626490, '2021-08-06', 9004)
]
details = [
 (9423517, 'Jeans', 'Rip Curl', 87.0, 1),
 (9423517, 'Jacket', 'The North Face', 112.0, 1),
 (4626232, 'Socks', 'Vans', 15.0, 1),
 (4626232, 'Jeans', 'Quiksilver', 82.0, 1),
 (9423534, 'Socks', 'DC', 10.0, 2),
 (9423534, 'Socks', 'Quiksilver', 12.0, 2),
 (9423679, 'T-shirt', 'Patagonia', 35.0, 1),
 (4626377, 'Hoody', 'Animal', 44.0, 1),
 (4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
 (4626412, 'Shirt', 'Volcom', 78.0, 1),
 (9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
 (9423783, 'Shorts', 'Globe', 26.0, 1),
 (4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
 (4626490, 'Sweater', 'Dickies', 56.0, 1)
]
df_orders = pd.DataFrame(orders, columns=['OrderNo','Date','Empno'])
df_details = pd.DataFrame(details, columns=['OrderNo','Item','Brand','Price','Quantity'])

df_details = df_details._append(
    {'OrderNo':4626592,
     'Item':'Shorts',
     'Brand':'Protest',
     'Price':48,
     'Quantity':1},
     ignore_index=True # this has to be set otherwise you won't be able to append a dict to a DataFrame
)

df_orders_details_right = df_orders.merge(df_details,how='right',on='OrderNo')
# the empty field will be fill in'NaN', which will result the column type change from int to float
# to covert back to int, we use below code
df_orders_details_right = df_orders_details_right.fillna({'Empno':0}).astype({'Empno':'Int64'})
# fillna method will replace NaNs in the specified column with a specific value.

# 3. implementing a Many-to-Many join
books = pd.DataFrame(
    {'book_id':['b1','b2','b3'],
     'title': ['Beautiful Coding','Python for Web Development','Pythonic Thinking'],
     'topic': ['programming','Python, Web', 'Python']})


authors = pd.DataFrame({'author_id':['jsn','tri','wsn'],
                        'author' : ['Johnson','Treloni','Willson']})

matching = pd.DataFrame({'author_id':['jsn','jsn','tri','wsn'],
                         'book_id':['b1','b2','b2','b3']})

authorship = books.merge(matching).merge(authors)[['title','topic','author']] # [['title','topic','author']] select 3 columns as a result

print(authorship)
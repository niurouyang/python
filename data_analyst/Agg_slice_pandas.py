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

import pandas as pd
df_orders = pd.DataFrame(orders, columns =['OrderNo','Date', 'Empno'])

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
#converting the list into a DataFrame
df_details = pd.DataFrame(details, columns =['OrderNo','Item', 'Brand', 'Price', 'Quantity'])

emps = [
 (9001, 'Jeff Russell', 'LA'),
 (9002, 'Nick Boorman', 'San Francisco'),
 (9003, 'Tom Heints', 'NYC'),
 (9004, 'Maya Silver', 'Philadelphia')
]

df_emps = pd.DataFrame(emps, columns =['Empno', 'Empname', 'Location'])

locations = [
 ('LA', 'West'),
 ('San Francisco', 'West'),
 ('NYC', 'East'),
 ('Philadelphia', 'East')
]

df_locations = pd.DataFrame(locations, columns =['Location','Region'])

df_sales = df_orders.merge(df_details)
df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
df_sales = df_sales[['Date','Empno','Total']]
df_sales_emps = df_sales.merge(df_emps)
df_result = df_sales_emps.merge(df_locations)
df_result = df_result[['Date','Region','Total']]

print(df_result)
df_date_region = df_result.groupby(['Date','Region']).sum()

df_date_region_1 = df_date_region[df_date_region.index.isin([('2021-08-05','West')])]
df_date_region_2 = df_date_region[df_date_region.index.isin([('2021-08-05','West'),('2021-08-05','East')])]
df_date_region_3 = df_date_region[('2021-08-04','East'):('2021-08-05','West')]
df_date_region_4 = df_date_region['2021-08-04':'2021-08-05']
df_date_region_5 = df_date_region.loc[(slice('2021-08-05','2021-08-06'),slice(None)),:]
# first slice for a specific slice of dates, second slice for all reigon(use None parameter)
# ,: specifies that you are using row labels rather than column lables, but it looks like this is default value
df_date_region_6 = df_date_region.loc[(slice('2021-08-05','2021-08-06'),slice('East')),:]

sales_total = df_date_region.sum()

sales_total.name = ('All','All')

df_date_region_total = df_date_region._append(sales_total)
df_date_region_total = df_date_region_total[df_date_region_total.index.isin([('All','All')])]
#print(df_date_region_total)

df_totals = pd.DataFrame()
for date, date_df in df_date_region.groupby(level=0):
    df_totals = df_totals._append(date_df)
    ps = date_df.sum(axis=0)
    ps.name = (date,'All')
    df_totals = df_totals._append(ps)
#print(df_totals)


group = df_result.groupby(['Date','Region'])
group_result = group.get_group(('2021-08-04','West'))
print(group_result)
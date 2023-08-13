from matplotlib import pyplot as plt

# plot the data on a line chart
days = ['2023-08-07','2023-08-08','2023-08-09','2023-08-10','2023-08-11']
prices = [250,245,240,245,240]
plt.plot(days,prices)
plt.title('NASDAQ:TSLA')
plt.xlabel('Date')
plt.ylabel('USD')
#plt.show()

# plot the data on a pie chart
regions = ['New England', 'Mid-Atlantic','Midwest']
sales = [882703, 532648,714406]
plt.pie(sales, labels=regions,autopct='%1.1f%%')
plt.title('Sales per Region')
#plt.show()

# plot the same data on a bar chart
regions = ['New England', 'Mid-Atlantic','Midwest']
sales = [882703, 532648,714406]
plt.bar(regions,sales)
plt.xlabel('Regions')
plt.ylabel('Sales')
plt.title('Annual Sales Aggregated on a Regional Basis')
#plt.show()

# create a figure and axe object(use subplot), and use them to manipulate visual view
import numpy as np
import matplotlib.ticker as ticker
# data to plot
salaries = [1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324, 1326, 1337, 1346, 1354, 1355, 1364, 1367, 1372, 1375, 1376, 1378, 1378, 1410, 1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437, 1451, 1454, 1467, 1470, 1473, 1477, 1479, 1480, 1514, 1516, 1522, 1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717]
# preparing a histogram
fig, ax = plt.subplots()
fig.set_size_inches(8.6, 6.2)
ax.hist(salaries, bins=np.arange(1100, 1900, 50), edgecolor='black',linewidth=1.2)
formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(formatter)
plt.title('Monthly Salaries in the Sales Department')
plt.xlabel('Salary (bin size = $50)')
plt.ylabel('Frequency')
# showing the histogram
#plt.show()

# making a pie chart by using subplot
count,labels = np.histogram(salaries, bins =np.arange(1100,1900,50))
# use histogram will return two Numpy arrays: count and labelss
# the count represents the nummber of employees with salaries in each interval [0,0,2,5...,0,0]
# the labels array contains the edges of the bin intervals [1100,1150,1200...,1850]
labels = ['$' +str(labels[i])+'-'+str(labels[i+1]) for i, _ in enumerate(labels[1:])]
non_zero_pos = [i for i, x in enumerate(count) if x != 0]
# to get rid of 0 inside the count array.
labels = [e for i,e in enumerate(labels) if i in non_zero_pos]
count = [e for i,e in enumerate(count) if i in non_zero_pos]
plt.pie(count,labels=labels,autopct='%1.1f%%')
plt.title('Monthly Salries in the Sales Department')
plt.show()

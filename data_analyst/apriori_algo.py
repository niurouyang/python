transactions = [
 ['curd', 'sour cream'], ['curd', 'orange', 'sour cream'],
 ['bread', 'cheese', 'butter'], ['bread', 'butter'], ['bread', 'milk'],
 ['apple', 'orange', 'pear'], ['bread', 'milk', 'eggs'], ['tea', 'lemon'],
 ['curd', 'sour cream', 'apple'], ['eggs', 'wheat flour', 'milk'],
 ['pasta', 'cheese'], ['bread', 'cheese'], ['pasta', 'olive oil', 'cheese'],
 ['curd', 'jam'], ['bread', 'cheese', 'butter'],
 ['bread', 'sour cream', 'butter'], ['strawberry', 'sour cream'],
 ['curd', 'sour cream'], ['bread', 'coffee'], ['onion', 'garlic']
]
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

encoder = TransactionEncoder()
encoded_array = encoder.fit(transactions).transform(transactions)
df_itemsets = pd.DataFrame(encoded_array, columns=encoder.columns_)

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df_itemsets, min_support= 0.1, use_colnames=True)

#you can't use frequent_itemsets['length'] = len(frequent_itemsets['itemsets']), because it will only return the length of the entire 'itemsets' column
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda itemset:len(itemset))
# this will give each row its itemset length
# print(frequent_itemsets[frequent_itemsets['length'] >=2])

from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)

rules_plot = pd.DataFrame()
rules_plot['antecedents'] = rules['antecedents'].apply(lambda x:','.join(list(x)))
rules_plot['consequents'] = rules['consequents'].apply(lambda x:','.join(list(x)))
rules_plot['lift'] = rules['lift'].apply(lambda x:round(x,2))

pivot = rules.pivot(index='antecedents',columns='consequents', values='lift')

antecedents = list(pivot.index.values)
consequents = list(pivot.columns)
import numpy as np
pivot  = pivot.to_numpy()

import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
im = ax.imshow(pivot,cmap = 'Reds')
ax.set_xticks(np.arange(len(consequents)))
ax.set_yticks(np.arange(len(antecedents)))
ax.set_xticklabels(consequents)
ax.set_yticklabels(antecedents)
plt.setp(ax.get_xticklabels(),rotation = 45, ha ='right',rotation_mode = 'anchor')
for i in range(len(antecedents)):
    for j in range(len(consequents)):
        if not np.isnan(pivot[i,j]):
            text = ax.text(j,i, pivot[i, j], ha ='center', va='center')
ax.set_title('life metric for frequent itemsets')
fig.tight_layout()
plt.show()
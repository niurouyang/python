data = [
{
    'EMP' : 'Wansheng Yang',
    'POs' : [
        {'Pono' : 1001, 'Total' : 30},
        {'Pono' : 1002, 'Total' : 40},
        {'Pono' : 1003, 'Total' : 45}
    ]
},
{
    'EMP' : 'Matthew Yang',
    'POs' :[
        {'Pono' : 1011, 'Total' : 100},
        {'Pono' : 1012, 'Total' : 50}
    ]
}
]

import json
import pandas as pd
df = pd.json_normalize(data,'POs','EMP') # the second argument is 'record_path' and the third argument is 'meta'
# record_path: Specifies the path to the records in the JSON structure that you want to normalize. This is especially useful when dealing with nested arrays.
# meta: Specifies additional columns to include in the DataFrame. These columns are not part of the nested JSON but provide context for the normalized data.
print(df)


df = df.reset_index()
json_doc = (df.groupby(['EMP'], as_index=True) # group by EMP, and use EMP as index
            .apply(lambda x: x[['Pono','Total']].to_dict('records')) # selects the columns 'Pono' and 'Total'
            # from dataframe x and convert the selected rows into a list of dictionaries. This expression is 
            # commonly used when you want to extract specific columns from a DataFrame and convert the selected 
            # rows into a list of dictionaries for further processing or formatting purposes.
            .reset_index()
            .rename(columns={0:'POs'})
            # Renaming the column with index '0' to the name 'POs'
            .to_json(orient='records')
)
print(json_doc)


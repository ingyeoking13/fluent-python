from pandas import DataFrame
import numpy as np

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data.loc[2,'col1']) 
data.loc[2,'col1'] = np.nan

print(data)
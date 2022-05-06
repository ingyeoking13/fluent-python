import pandas as pd 
import numpy as np

df = pd.DataFrame(
    [["bar", "one"], ["foo", "one"], ["foo", "two"]],
    columns=["first", "second"],
)
# print(df)

# arrays = pd.DataFrame(
#     [["bar", "one"], ["bar", "one"], ["baz", "two"], ["baz", "one"], 
#     ["foo", "two"], ["foo", "one"], ["qux", "two"], ["qux" "one"]],
#     columns=["date", "covCd"]
# )

result = pd.MultiIndex.from_frame(df)

print(result)



df = pd.DataFrame(np.random.randn(3, 3), index=result, columns=['col1', 'col2', 'col3'])

print(df.get('colr'))

_mydict = {"계산값" : df }
print(df)
print(_mydict['계산값'])

# import packages
import pandas as pd
from tqdm import tqdm

# load data
df = pd.read_csv('test_output/Link_example_1.csv', encoding='cp949')
print(df.head())

# 
for idx, v in enumerate(df['L7']):
    if v != 0:
        print('LINK_ID :', df['LINK_ID'][idx])
        print(v)
        
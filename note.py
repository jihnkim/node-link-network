
# load data
# import packages
from os import link
import pandas as pd
from tqdm import tqdm
from CheckSum import checkSum

# load data
df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/test/link_링크별구역_7_1구역.csv', encoding='cp949')
df = df.iloc[:]
lamp_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/test/lamp_links.csv', encoding='cp949')
lamp_df = lamp_df[lamp_df['T'].isin(['램프구간'])]

# print(df.head())
# print(lamp_df)
print(df.iloc[:10])
print(list(df['LINK_ID'])[:5])
# cnt = 0
# for idx, l in tqdm(enumerate(list(df['LINK_ID']))):
#     if l in list(lamp_df['LINK_ID']):
#         df['CHK'][idx] = 3
#         cnt += 1

# print(cnt)
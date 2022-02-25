#-*- coding: utf-8 -*-
'''
    @ Author : jihnkim
    @ method : check & fill empty col value
'''
# import packages
import pandas as pd
from tqdm import tqdm

# load data
link_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/data/LINK_3.csv', encoding='cp949')

# main logic
for i in tqdm(range(len(link_df))):
    L_lst = []
    for j in range(1, 7):
        lnk = link_df[f'L{j}'][i]
        if lnk != 0:
            L_lst.append(lnk)
            link_df[f'L{j}'][i] = 0
    
    for idx, v in enumerate(L_lst):
        link_df[f'L{idx + 1}'][i] = v

# check empty col
for i in range(1, 8):
    cnt = len(link_df[link_df[f'L{i}'].isin([0])])
    print(f'L{i} : {cnt}')

# check method
def CheckEmptyLink(df):
    df = df[df['L1'].isin([0])]
    df.to_csv('공백제거후확인용.csv', index=False)
    pass

link_df.to_csv('확인용.csv', index=False)

# if __name__ == '__main__':
#     pass
#-*- coding: utf-8 -*-
'''
    @ Author : jihnkim
    @ method : col value summation
'''

# import packages
import pandas as pd
from tqdm import tqdm

# load data
# df = pd.read_csv('test_output/Link_example_1.csv', encoding='cp949')
# print(df.head())

# check col value & count
def checkSum(df, colname, adj_value_lst):
    cnt = 0
    for idx, v in enumerate(df[colname]):
        if v in adj_value_lst:
            # print('LINK_ID :', df['LINK_ID'][idx])
            # print(v)
            cnt += 1

    return cnt

# if __name__ == '__main__':
    # cnt = checkSum(df, 'CHK', [3, 4])
    # print('SUM :', cnt)
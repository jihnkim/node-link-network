#-*- coding: utf-8 -*-
'''
    @ Author : jihnkim
    @ method : remove link in turninfo table
'''

# import packages
from numpy import int64
import pandas as pd
from tqdm import tqdm

# load data
INPUT_DIR = ''
OUPUT_DIR = ''

link_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/data/LINK_3.csv', encoding='cp949')
link_df = link_df.loc[:, ['LINK_ID', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7']]
link_df = link_df.fillna(0)
link_df = link_df.astype(int64)

print(link_df.head(), 'DATAFRAME LENGTH : ', len(link_df))
print('TYPE : ', link_df.dtypes)

turn_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/data/TURNINFO.csv', encoding='cp949')
turn_df['TURN_TYPE'] = turn_df['TURN_TYPE'].astype(int64)

print(turn_df.head(), 'DATAFRAME LENGTH : ', len(turn_df))
print('TYPE : ', turn_df.dtypes)

# check dataset
# remove without (003, 101, 102, 103) in turninfo csv
print('BEFORE DATAFRAME LENGTH : ', len(turn_df))

CHK_LST = ['003', '101', '102', '103']
CHK_LST2 = [3, 101, 102, 103]

# .isin() method return TRUE, FALSE table
turn_df = turn_df[turn_df['TURN_TYPE'].isin(CHK_LST2)]

print('REMOVED DATAFRAME LENGTH : ', len(turn_df))

# sorting for optimize complexity
print('SORTING START . . .')

link_df = link_df.sort_values('LINK_ID')
link_df = link_df.reset_index(drop=True)
turn_df = turn_df.sort_values('ST_LINK')
turn_df = turn_df.reset_index(drop=True)

print(link_df.head())
print(turn_df.head())

# main Logic
# df length
len_turndf = len(turn_df['NODE_ID'])
len_linkdf = len(link_df['LINK_ID'])

# index mark
link_idx = 0
for i in tqdm(range(len_turndf)):
    ST_LINK = turn_df['ST_LINK'][i]
    ED_LINK = turn_df['ED_LINK'][i]
    # if st_link == link_id >> remove L1, L2, ... which include ed_link
    for j in range(link_idx, len_linkdf):
        if ST_LINK == link_df['LINK_ID'][j]:
            # index reallocation(cause.. sorted table >> about before-idx, no need to consider)
            link_idx = j
            for cnt in range(1, 8):
                if ED_LINK == link_df[f'L{cnt}'][j]:
                    link_df[f'L{cnt}'][j] = 0
                    break
            # why use break command? >> LINK_ID is UNIQUE VALUE
            break

print(link_df.dtypes)

link_df.to_csv('????????????????????????_LINK.csv', index=False)

print('CSV SAVED')
# consider
# 회전타입 지울 때 컬럼 밸류가 003, 101, 102, 103 인것만 지워야함
# 처음 테이블 잡을 때  행 날리자

# import packages
from numpy import int64
import pandas as pd
from tqdm import tqdm

# load data
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
print('FINISH')

# main Logic
# turn_df 에서 ST_LINK 하나씩 뽑자
len_turndf = len(turn_df['NODE_ID'])
len_linkdf = len(link_df['LINK_ID'])

link_idx = 0
for i in tqdm(range(len_turndf)):
    ST_LINK = turn_df['ST_LINK'][i]
    ED_LINK = turn_df['ED_LINK'][i]
    # link df 에서 L1, L2, L3 .. 값들 중 ED_LINK와 같은 값이 있는 지 체크 있다면 제거
    for j in range(link_idx, len_linkdf):
        if ST_LINK == link_df['LINK_ID'][j]:
            link_idx = j
            for cnt in range(1, 8):
                if ED_LINK == link_df[f'L{cnt}'][j]:
                    link_df[f'L{cnt}'][j] = 0
                    break
            break

print(link_df.dtypes)

link_df.to_csv('회전금지제거최종_LINK.csv', index=False)

print('CSV SAVED')
# consider
# 회전타입 지울 때 컬럼 밸류가 003, 101, 102, 103 인것만 지워야함
# 처음 테이블 잡을 때  행 날리자

# import packages
import pandas as pd
from tqdm import tqdm

# load data
link_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/data/LINK.csv', encoding='cp949')
print(link_df.head(), 'DATAFRAME LENGTH : ', len(link_df))
turn_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/data/TURNINFO.csv', encoding='cp949')
print(turn_df.head(), 'DATAFRAME LENGTH : ', len(turn_df))

# check dataset
# remove without (003, 101, 102, 103) in turninfo csv


# sorting for optimize complexity
print('SORTING START . . .')
link_df.sort_values('LINK_ID')
turn_df.sort_values('LINK_ID')
print(link_df.head())
print(turn_df.head())
print('FINISH')

# main Logic
# turn_df 에서 ST_LINK 하나씩 뽑자
len_turndf = len(turn_df['NODE_ID'])
len_linkdf = len(link_df['LINK_ID'])

for i in tqdm(range(len_turndf)):
    ST_LINK = turn_df['ST_LINK'][i]
    ED_LINK = turn_df['ED_LINK'][i]
    # link df 에서 L1, L2, L3 .. 값들 중 ED_LINK와 같은 값이 있는 지 체크 있다면 제거
    for j in range(len_linkdf):
        if ST_LINK == link_df['LINK_ID'][j]:
            if ED_LINK == link_df['L1'][j]:
                link_df.iloc[j, 17] = 0
            if ED_LINK == link_df['L2'][j]:
                link_df.iloc[j, 18] = 0
            if ED_LINK == link_df['L3'][j]:
                link_df.iloc[j, 19] = 0
            if ED_LINK == link_df['L4'][j]:
                link_df.iloc[j, 20] = 0
            break

print(link_df.dtypes)

link_df.to_csv('회전금지제거최종_LINK.csv', index=False)

print('CSV SAVED')
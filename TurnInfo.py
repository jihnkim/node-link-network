# import packages
import pandas as pd
from tqdm import tqdm

# load data
link_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/LINK.csv', encoding='cp949')
print(link_df.head())
turn_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/turninfo.csv', encoding='cp949')
print(turn_df.head())

# check empty col

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
                link_df.iloc[j, 17] = ' '
            if ED_LINK == link_df['L2'][j]:
                link_df.iloc[j, 18] = ' '
            if ED_LINK == link_df['L3'][j]:
                link_df.iloc[j, 19] = ' '
            if ED_LINK == link_df['L4'][j]:
                link_df.iloc[j, 20] = ' '

print(link_df.dtypes)

link_df.to_csv('회전금지제거_LINK.csv', index=False)





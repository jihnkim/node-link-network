import pandas as pd
from tqdm import tqdm
from CheckSum import checkSum

# 램프구간도 기존 로직대로 돌리고 추후에 arcGIS툴로 제거 
df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/test/lamp_links.csv', encoding='cp949')

# 빈 컬럼 세팅
for n in range(1, 9):
    df[f'L{n}'] = 0
df['CHK'] = 0

# 사용할 열 선택
df = df.loc[:, ['LINK_ID', 'F_NODE', 'T_NODE', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'CHK']]

# main logic
for idx in tqdm(range(len(df['LINK_ID']))):
    # print('==', 'LINK ID : ', df['LINK_ID'][idx], '==')
    F_NODE = df['F_NODE'][idx]
    T_NODE = df['T_NODE'][idx]
    CHK = 2
    u = []
    lst = []
    
    # LINK ID 비교 로직
    for j in range(len(df['LINK_ID'])):
        # 비교 LINK_ID가 같은 행 건너 뛰기
        if idx == j:
            continue

        # 다음 경로 링크 찾기
        if T_NODE == df['F_NODE'][j]:

            # 유턴일 경우 임시 리스트에 저장
            if F_NODE == df['T_NODE'][j]:
                u.append(df['LINK_ID'][j])
                continue
            
            # 유턴이 아닌 링크가 있을 경우 리스트에 저장
            lst.append(df['LINK_ID'][j])
            CHK = 1

    # 특수링크
    if (len(lst) == 0) and (len(u) == 0):
        CHK = 4

    # 최종 리스트 요소를 L1, L2, L3 .. 에 추가 하는 로직, 최종 df 반환 (list -> dataFrame)
    if CHK == 1:
        cnt = 1
        for link in lst:
            df[f'L{cnt}'][idx] = link
            cnt += 1
    
    if CHK == 2:
        df['L1'][idx] = u[0]

    df['CHK'][idx] = CHK

CNT = checkSum(df, 'CHK', [1, 2])
print(f"SUM : {CNT}", f'/ {len(df)}')

df.to_csv(f'test_output/lamp_link_need_remove.csv', index=False)
print(" == CSV SAVED == ")

# import packages
import pandas as pd
from tqdm import tqdm
from CheckSum import checkSum

for filenum in range(2, 9):
    # load data
    df = pd.read_csv(f'C:/Users/jih11/Desktop/myprojects/ybs/test/link_링크별구역_7_{filenum}구역.csv', encoding='cp949')
    lamp_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/test/lamp_links.csv', encoding='cp949')
    lamp_df = lamp_df[lamp_df['T'].isin(['램프구간'])]
    # print(df.head())
    # print(lamp_df.head())

    # 확인용 데이터 세팅 (필요시 진행)
    # df = df.iloc[0:]
    # print(df)

    # 빈 컬럼 세팅
    for n in range(1, 9):
        df[f'L{n}'] = 0
    df['CHK'] = 0
    # print(df.head())

    # 사용할 열 선택
    df = df.loc[:, ['LINK_ID', 'F_NODE', 'T_NODE', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'CHK']]
    # print(df.head())

    # 다음 경로 열 공백 처리 (필요시 진행)
    # df.loc[:, ['L1', 'L2', 'L3', 'L4', 'L5', 'L6']] = ' '
    # print(df.head())

    # main logic
    for idx in tqdm(range(len(df['LINK_ID']))):
        # print('==', 'LINK ID : ', df['LINK_ID'][idx], '==')
        F_NODE = df['F_NODE'][idx]
        T_NODE = df['T_NODE'][idx]
        CHK = 2
        u = []
        lst = []
        fnode_lst = []
        tnode_lst = []
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
                fnode_lst.append(df['F_NODE'][j])
                tnode_lst.append(df['T_NODE'][j])

                CHK = 1

        # 램프형 / 마름모형 예외 처리 -> (fnode - tnode) 와 (tnode - fnode) 같은 링크가 존재하지 않는 특징 이용(고유값을 가짐)
        # for i in range(len(lst)):
        #     tmp = df[df['T_NODE'].isin([fnode_lst[i]]) & df['F_NODE'].isin([tnode_lst[i]])]
        #     if len(tmp) > 1:
        #         CHK = 3
        #         break

        # 이도저도 아닌 특수링크 표시
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
    print("CHECK LAMP SECTOR ... ")

    # 완성된 테이블에서 램프구간 제거
    for idx, l in tqdm(enumerate(list(df['LINK_ID']))):
        if l in list(lamp_df['LINK_ID']):
            df['CHK'][idx] = 3

    print("REMOVE FINISHED ... ")
    print(f"BEFORE REMOVE : {CNT}", f'/ {len(df)}')

    CNT = checkSum(df, 'CHK', [1, 2])
    print(f"AFTER REMOVE : {CNT}", f'/ {len(df)}')

    df.to_csv(f'test_output/Link_7_{filenum}.csv', index=False)
    print(" == CSV SAVED == ")
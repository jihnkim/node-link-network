import pandas as pd
from FillBlank import CheckEmptyLink

# main
if __name__ == '__main__':
    link_df = pd.read_csv('C:/Users/jih11/Desktop/myprojects/ybs/전국최종링크_공백제거.csv', encoding='cp949')
    CheckEmptyLink(link_df)
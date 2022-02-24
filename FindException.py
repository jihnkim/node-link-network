'''
    @ Author : jihnkim
    @ method : CHK <> 1 OR 2 
'''

# import packages
import pandas as pd
from tqdm import tqdm
from CheckSum import checkSum

# load data
FILE_DIR = ''
df = pd.read_csv(f'{FILE_DIR}', encoding='cp949')
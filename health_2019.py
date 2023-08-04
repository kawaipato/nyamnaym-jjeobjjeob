import pandas as pd

health_data_2019 = pd.read_csv('2019년 건강검진정보(전처리).csv')
health_data_2019 = health_data_2019.drop(['Unnamed: 0'],axis=1)
# 총 콜레스테롤 결측치 제거
total_col = health_data_2019.dropna(subset=['총 콜레스테롤'])
total_col.index = range(1,len(total_col)+1)
total_col.to_csv('delete total cholesterol.csv')

#  LDL 결측치 제거
LDL_col = health_data_2019.dropna(subset=['LDL 콜레스테롤'])
LDL_col.index = range(1,len(LDL_col)+1)
LDL_col.to_csv('delete ldl cholesterol.csv')


# HDL 결측치 제거
HDL_col = health_data_2019.dropna(subset=['HDL 콜레스테롤'])
HDL_col.index = range(1,len(HDL_col)+1)
HDL_col.to_csv('delete hdl cholesterol.csv')


import pandas as pd
import warnings

warnings.filterwarnings('ignore')
# 프렌차이즈 리스트 불러오기
franchise_korea = pd.read_csv('../franchise_list/franchiseKfood.csv', encoding='cp949') #1531
franchise_china = pd.read_csv('../franchise_list/franchise중식.csv') #100
franchise_japan = pd.read_csv('../franchise_list/franchise일식.csv') #201
franchise_us = pd.read_csv('../franchise_list/franchise양식.csv') #141
franchise_etc = pd.read_csv('../franchise_list/franchise기타외국식.csv') #97
franchise_bread = pd.read_csv('../franchise_list/franchise제과제빵.csv')
franchise_drink = pd.read_csv('../franchise_list/franchise주점.csv')
franchise_fastfood = pd.read_csv('../franchise_list/franchise패스트푸드.csv')
franchise_chicken = pd.read_csv('../franchise_list/franchise치킨.csv')
franchise_coffee = pd.read_csv('../franchise_list/franchise커피외음료.csv')
franchise_pizza = pd.read_csv('../franchise_list/franchise피자.csv')
franchise_coffee2 = pd.read_csv('../franchise_list/franchise커피.csv')
franchise_icecream = pd.read_csv('../franchise_list/franchise아이스크림빙수.csv')
franchise_etc2 = pd.read_csv('../franchise_list/franchise기타외식.csv')
franchise_bunsic = pd.read_csv('../franchise_list/franchise분식.csv')

franchise_all = [franchise_korea,franchise_china,franchise_japan,franchise_us,franchise_etc,
                 franchise_bread,franchise_drink,franchise_fastfood,franchise_chicken,franchise_coffee,
                 franchise_pizza,franchise_coffee2,franchise_icecream,franchise_etc2,franchise_bunsic]

# 프랜차이즈 리스트들 하나로 합치기
franchise_list = pd.concat(franchise_all,ignore_index=True)
store_name = franchise_list['영업표지']

#부산 데이터들 합치기
busan1 = pd.read_csv('Busan_list/부산광역시 메뉴정보_2021_12.csv') #약 18만개
busan2 = pd.read_csv('Busan_list/부산광역시_7개 해수욕장 음식점 메뉴정보_2022_01.csv', encoding='cp949') # 약 6만개
data_list = [busan1, busan2]

busan = pd.concat(data_list, ignore_index=True)
busan.drop_duplicates('식당(ID)') #  중복제거

busan.index = range(0,len(busan))
delete_busan = busan[~busan['식당명'].isin(store_name)].to_csv('busan_dropped_franchise_data.csv',index=False)




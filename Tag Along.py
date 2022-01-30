import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://github.com/HamoyeHQ/HDSC-Introduction-to-Python-for-machine-learning/files/7768140/FoodBalanceSheets_E_Africa_NOFLAG.csv'


food_data = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'Latin-1')
food_data.isnull().sum()
feature_list = []
for i in food_data:
    feature_list.append(i)
    
feature_list

len(food_data)
# question 11
food_data.groupby('Item')['Y2014'].sum()
food_data.groupby('Item')['Y2017'].sum()
#(af_2014 = 209460.54, af_2017 = 269617.53)

# question 12
description = food_data.describe(include='all')

# question 13

food_data.isnull().sum()

# question 14

corrolation = food_data.corr()

# question 15

food_data.groupby('Element')['Y2018'].sum()

# 2014 = 274144.48
# 2015 = 267018.46
# 2016 = 286582.78
# 2017 = 294559.09
# 2018 = 287997.09

# question 16

food_data.groupby('Element')['Y2014'].sum()

# question 17 and 18
food_data.groupby('Element')['Y2018'].sum()

# question 19

food_data_algeria = food_data.iloc[:1313]
food_data_algeria.groupby('Element')['Y2018'].sum()

# question 20

len(food_data.groupby('Area')['Area'])

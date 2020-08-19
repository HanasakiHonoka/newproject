# encoding: utf-8
import numpy as np
import pandas as pd
from scipy.stats import norm, skew
import json
pd.set_option('display.width', 1200)

pd.set_option('display.max_rows', 4000)

pd.set_option('display.max_columns', 200)

df_train = pd.read_csv('premodel.csv')

df = df_train.copy(deep = True)
df = df[df['boxoffice'] >= 100]

Y0 = df['boxoffice']
Y1 = np.log1p(df['boxoffice'] * 10000)
Y2 = df['boxoffice'] * 10000
Y = Y0

df_input = df.copy(deep = True)
df_input.drop(['id','title','technology','type','boxoffice','first_boxoffice','actor','issue_company','manu_company','release_date','type_list','technology_list'],axis=1,inplace=True)


df_input.apply(lambda x: skew(x.dropna())).sort_values(ascending=False)
year_cols = ['year_2000','year_2001','year_2002','year_2003','year_2004',
             'year_2005','year_2006','year_2007','year_2008','year_2009',
             'year_2010','year_2011','year_2012','year_2013','year_2014',
             'year_2015','year_2016','year_2017','year_2018','year_2019']

genre_cols=['genre_剧情','genre_爱情','genre_喜剧','genre_动作','genre_惊悚',
      'genre_动画','genre_悬疑','genre_冒险','genre_犯罪','genre_战争',
      'genre_恐怖','genre_奇幻','genre_儿童','genre_纪录片','genre_青春']

df_baseline_input = df_input.copy(deep = True)
df_baseline_input.drop(year_cols,axis=1,inplace=True)
df_baseline_input.drop(['is_weekend','springfestival','nationalday','summer'],axis=1,inplace=True)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train,y_val = train_test_split(df_baseline_input,Y,test_size=0.3,random_state=78)

print(X_val.head())

from sklearn.linear_model import LinearRegression

LR=LinearRegression()

LR.fit(X_train,y_train)

print('训练集准确率：\n',LR.score(X_train, y_train)) # 分数
print('验证集准确率：\n',LR.score(X_val, y_val))

json_str = X_val.head().to_json(orient='index')
print(json_str)
y_baseline_pred_LR =(LR.predict(X_val.head())).astype(int)


raw_json = '''
{"11":{
    "duration": 90,
    "year": 2009,
    "month": 9,
    "day": 25,
    "day_of_week": 4,
    "quarter": 3,
    "week": 39,
    "num_types": 1,
    "genre_剧情": 1,
    "genre_爱情": 0,
    "genre_喜剧": 0,
    "genre_动作": 0,
    "genre_惊悚": 0,
    "genre_动画": 0,
    "genre_悬疑": 0,
    "genre_冒险": 0,
    "genre_犯罪": 0,
    "genre_战争": 0,
    "genre_恐怖": 0,
    "genre_奇幻": 0,
    "genre_儿童": 0,
    "genre_纪录片": 0,
    "genre_青春": 0,
    "technology_2D": 1,
    "technology_3D": 0,
    "technology_IMAX": 0
}}
'''
dt1 = pd.read_json(raw_json, orient='index')
print(LR.predict(dt1).astype(int))

# print(y_baseline_pred_LR)
# encoding: utf-8

# from win10toast import ToastNotifier
#
# tos = ToastNotifier()
#
# tos.show_toast(duration=1)
import json
import pandas as pd
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
test_data = json.loads(raw_json)
print(type(test_data))
pd.read_json(raw_json)
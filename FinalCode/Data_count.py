import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

with open("C:/ModuleProject1/FacebookProject/FinalCode/naverdata/naver_news_data.json", "r", encoding='utf-8') as filedata:
    newsdata = json.loads(filedata.read())

# pubDate 기준으로 정렬
sorted_arr = sorted(newsdata, key=lambda x: (x['pubDate']))
# print(sorted_arr)

now = datetime.now()    # 현재
date_year = "year" 
date_month = "month" 
date_week = "week" 
date_day = "day"

# 날짜 구간 조정
set_year = 3
set_month = 2
set_week = 1
set_day = 2

before_day = now - relativedelta(days=set_day)   # num일 전
before_week = now - relativedelta(weeks=set_week)   # num주 전
before_month = now - relativedelta(months=set_month)   # num달 전
before_year = now - relativedelta(years=set_year)   # num년 전

result = {"day":0, "week":0, "month":0, "year":0}
for i in result:
    for j in sorted_arr:
        if datetime.strptime(j['pubDate'], '%Y-%m-%d %H:%M:%S') < before_day  # pubDate 키의 값을 datetime 형식으로 변환
            continue
        else:
            # print(j['pubDate'])
            if (i in j['title']) or (i in j['description']) :
                result[i] += j['title'].count(i)
                result[i] += j['description'].count(i)

    print("keyword : 코로나 day : %d, week : %d, month : %d, year : %d" %(i, result[i]))
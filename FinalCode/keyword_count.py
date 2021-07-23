import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

with open("C:/LAB/DataLab/Module01/FinalCode/naverdata/naver_news_data.json", "r", encoding='utf-8') as filedata:
    newsdata = json.loads(filedata.read())

# pubDate 기준으로 정렬
sorted_arr = sorted(newsdata, key=lambda x: (x['pubDate']))
# print(sorted_arr)

keyword = "MZ세대"
now = datetime.now()    # 현재

# 날짜 구간 조정
before_day = now - relativedelta(days=1)   # 1일 전
before_week = now - relativedelta(weeks=1)   # 1주 전
before_month = now - relativedelta(months=1)   # 1달 전
before_year = now - relativedelta(years=1)   # 1년 전

result = {"day":0, "week":0, "month":0, "year":0}

for i in sorted_arr:    
    pubDate = datetime.strptime(i['pubDate'], '%Y-%m-%d %H:%M:%S')  # pubDate 키의 값을 datetime 형식으로 변환
    if (keyword in i['title']) or (keyword in i['description']):
        if before_day <= pubDate:  
            result['day'] = result['day'] + i['title'].count(keyword) + i['description'].count(keyword)
        if before_week <= pubDate: 
            result['week'] = result['week'] + i['title'].count(keyword) + i['description'].count(keyword)
        if before_month <= pubDate: 
            result['month'] = result['month'] + i['title'].count(keyword) + i['description'].count(keyword)
        if before_year <= pubDate: 
            result['year'] = result['year'] + i['title'].count(keyword) + i['description'].count(keyword)
    else:
        continue
        
print("keyword : %s\nday : %d, week : %d, month : %d, year : %d" %(keyword, result['day'], result['week'], result['month'], result['year']))

'''
모 듈 명 : keyword_count.py
작 성 자 : 이용하, 박준용, 윤상우 
작 성 일 : 2021.07.23
정    의 : 뉴스 데이터를 가져와 날짜 구간, 키워드를 입력 후 키워드 수 카운트 
'''
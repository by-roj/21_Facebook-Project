import json
from collections import OrderedDict

with open("C:/Users/user/LYH/ModuleProject1/FacebookProject/news_data.json", "r", encoding='utf-8') as filedata:
    newsdata = json.loads(filedata.read())

# pubDate 기준으로 정렬
sorted_arr = sorted(newsdata, key=lambda x: (x['pubDate']))
# print(sorted_arr)

startDate = '2021-07-21 12:00:00'
endDate = '2021-07-21 13:00:00'

result = {"코로나":0, "올림픽":0, "폭염":0}

for i in result:
    for j in sorted_arr:
        if j['pubDate'] < startDate:
            continue
        else:
            if j['pubDate'] > endDate:
                break

            if i in j['title']:
                result[i] += j['title'].count(i)

    print("keyword : %s, count : %d" %(i, result[i]))
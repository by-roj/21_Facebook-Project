import json
import matplotlib.pyplot as plt
from matplotlib import font_manager

with open("./data/news_data.json", "r", encoding='utf-8') as filedata:
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

            if (i in j['title']) or (i in j['description']) :
                result[i] += j['title'].count(i)
                result[i] += j['description'].count(i)

    print("keyword : %s, count : %d" %(i, result[i]))

news_data = list(result.items())

fontLocation = r"C:\Windows\Fonts\malgun.ttf"
fontName = font_manager.FontProperties(fname=fontLocation).get_name()
plt.rc('font', family=fontName)

plt.plot([i[0] for i in news_data], [i[1] for i in news_data], 'r')
plt.title('해시태그별 기사 수')
plt.xlabel('해시태그')
plt.ylabel('기사 수')
plt.show()
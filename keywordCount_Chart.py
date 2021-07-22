import json
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

fontLocation = r"C:\Windows\Fonts\malgun.ttf"
fontName = font_manager.FontProperties(fname=fontLocation).get_name()
plt.rc('font', family=fontName)

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

            if (i in j['title']) or (i in j['description']) :
                result[i] += j['title'].count(i)
                result[i] += j['description'].count(i)

    print("keyword : %s, count : %d" %(i, result[i]))

news_data = list(result.items())

# Pie Chart
# fig = plt.figure(figsize=(5,5)) # 캔버스 생성
# fig.set_facecolor('white') # 캔버스 배경색을 하얀색으로 설정
# ax = fig.add_subplot() # 프레임 생성

# labels = []
# frequency = []
# for x, y in news_data:
#     labels.append(x)
#     frequency.append(y)

# pie = ax.pie([i[1] for i in news_data],
#             startangle=90,
#             counterclock=False,
#             autopct=lambda p : '{:.2f}%'.format(p),
#             wedgeprops=dict(width=1),
#             colors=['cornflowerblue', 'yellowgreen', 'salmon'])

# plt.legend(pie[0], [i[0] for i in news_data])
# plt.show()

# Bar Chart
# n_groups = len([i[1] for i in news_data])
# index = np.arange(n_groups)

# plt.bar(index, [i[1] for i in news_data], tick_label=[i[0] for i in news_data], align='center')

# plt.xlabel('word')
# plt.ylabel('frequency')
# plt.title('News KeyWord Bar Chart')
# plt.xlim( -1, n_groups)
# plt.ylim( 0, 150)
# plt.show()

# Line Chart
plt.plot([i[0] for i in news_data], [i[1] for i in news_data], 'r')
plt.title('해시태그별 기사 수')
plt.xlabel('해시태그')
plt.ylabel('기사 수')
# plt.axis([0,10, 0, 110])
plt.show()
import matplotlib.pyplot as plt
from matplotlib import font_manager

fontLocation = r"C:\Windows\Fonts\malgun.ttf"
fontName = font_manager.FontProperties(fname=fontLocation).get_name()
plt.rc('font', family=fontName)

# news_labels = ('코로나', '올림픽', '폭염', '비트코인', '주식', '방역', '거리두기', 'MZ세대', '전세', '집값')
# news_frequency = (100, 20, 56, 76, 54, 94, 73, 82, 68, 47)

news_data = (('코로나',100), ('올림픽',20), ('폭염',56), ('비트코인',76), ('주식',54), ('방역',94), ('거리두기',73), ('MZ세대',82), ('전세',68), ('집값',47 ))

fig = plt.figure(figsize=(5,5)) # 캔버스 생성
fig.set_facecolor('white') # 캔버스 배경색을 하얀색으로 설정
ax = fig.add_subplot() # 프레임 생성

news_data = sorted(news_data, key=(lambda x:x[1]))
labels = []
frequency = []
for x, y in news_data:
    labels.append(x)
    frequency.append(y)

pie = ax.pie(frequency,
            startangle=90,
            counterclock=False,
            autopct=lambda p : '{:.2f}%'.format(p),
            wedgeprops=dict(width=1))

plt.legend(pie[0], labels)
plt.show()
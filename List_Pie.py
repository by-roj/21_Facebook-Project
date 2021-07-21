import matplotlib.pyplot as plt
from matplotlib import font_manager

fontLocation = r"C:\Windows\Fonts\malgun.ttf"
fontName = font_manager.FontProperties(fname=fontLocation).get_name()
plt.rc('font', family=fontName)

news_labels = ['코로나', '올림픽', '폭염', '비트코인', '주식', '방역', '거리두기', 'MZ세대', '전세', '집값']
news_frequency = [100, 20, 56, 76, 54, 94, 73, 82, 68, 47]

fig = plt.figure(figsize=(8,8)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 배경색을 하얀색으로 설정
ax = fig.add_subplot() ## 프레임 생성

pie = ax.pie(news_frequency,
            startangle=90,
            counterclock=False,
            autopct=lambda p : '{:.2f}%'.format(p),
            wedgeprops=dict(width=1))

plt.legend(pie[0], news_labels)
plt.show()
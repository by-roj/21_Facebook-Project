from matplotlib import font_manager
import matplotlib
import matplotlib.pylab as plt

fronLocation = "C:\Windows\Fonts\malgun.ttf"
fornName = font_manager.FontProperties(fname=fronLocation).get_name()
matplotlib.rc('font',family=fornName)


news_data = {'코로나':60, '올림픽':80, '폭염':67, '비트코인':43, '주식':50, '방역':76, '거리두기':70, 'MZ세대':30, '전세':21, '집값':47 }

Data = news_data.items()
myList = sorted(Data)
x, y = zip(*Data)

plt.plot(x, y, 'r') 
plt.xlabel('해시태그')
plt.ylabel('기사 수')
plt.title('연합뉴스 해시태그별 기사 수')
plt.axis([0,10, 0, 110]) # x: 0 ~ 150, y:0 ~ 10
plt.show()
plt.subplots_adjust(hspace=11)
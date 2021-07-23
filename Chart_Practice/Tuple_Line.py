from matplotlib import font_manager
import matplotlib.pyplot as plt
import matplotlib

fronLocation = "C:\Windows\Fonts\malgun.ttf"
fornName = font_manager.FontProperties(fname=fronLocation).get_name()
matplotlib.rc('font',family=fornName)

해시태그 = ('코로나', '올림픽', '폭염', '비트코인', '주식', '방역', '거리두기', 'MZ세대', '전세', '집값')
기사수 = (60, 80, 43, 50, 76, 70, 30, 21, 47, 20)

plt.plot(해시태그, 기사수, 'r')
plt.title('연합뉴스 해시태그별 기사 수')
plt.xlabel('해시태그')
plt.ylabel('기사수')
plt.axis([0,10, 0, 110])
plt.show()()
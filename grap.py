import matplotlib.pylab as plt

news_data = {'코로나':100, '올림픽':20, '폭염':56, '비트코인':76, '주식':54, '방역':94, '거리두기':73, 'MZ세대':82, '전세':68, '집값':47 }

myList = news_data.items()
myList = sorted(myList)
x, y = zip(*myList)

plt.plot(x, y)
plt.xlabel('Key')
plt.ylabel('Value')
plt.title('My Dictionary')
plt.show()
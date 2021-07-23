import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import platform
import sys

if sys.platform in ["win32", "win64"] :
    font_name = "malgun gothic"
elif sys.platform == "darwin" :
    font_name = "AppleGothic"
rc('font', family=font_name)

# 여기부터는 가로 Bar
x = np.arange(10)
word = [ '코로나', '올림픽', '폭염', '비트코인', '주식', '방역', '거리두기', 'MZ세대', '전세', '집값' ]
values = [100, 20, 56, 76, 54, 94, 73, 82, 68, 47]


plt.figure(figsize=(10, 8))
plt.bar(x, values)
plt.xticks(x, word)
plt.show()




"""
# 여기부터는 세로 Bar~~입니다 
y = np.arange(10)
word = [ '코로나', '올림픽', '폭염', '비트코인', '주식', '방역', '거리두기', 'MZ세대', '전세', '집값' ]
values = [100, 20, 56, 76, 54, 94, 73, 82, 68, 47]

plt.barh(y, values, height=-0.6, align='edge', color="springgreen",
        edgecolor="gray", linewidth=3, tick_label=word, log=False)
plt.show()

"""
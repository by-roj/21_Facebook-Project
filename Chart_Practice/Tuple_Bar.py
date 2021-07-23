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

values = (100, 20, 56, 76, 54, 94, 73, 82, 68, 47)
word=('코로나', '올림픽', '폭염', '비트코인', '주식', '방역', '거리두기', 'MZ세대', '전세', '집값' )
n_groups = len(word)
index = np.arange(n_groups)

plt.bar(index, values, tick_label=word, align='center')

plt.xlabel('word')
plt.ylabel('statistics')
plt.title('News KeyWord Bar Chart')
plt.xlim( -1, n_groups)
plt.ylim( 0, 100)
plt.show()
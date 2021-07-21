import json

with open("C:/Lab/hot_naver_news.json", encoding='utf-8') as file_1:
	data1 = json.loads(file_1.read())

with open("C:\Lab\corona_naver_news.json", encoding='utf-8') as file_2:
	data2 = json.loads(file_2.read())

with open("C:\Lab\olympic_naver_news.json", encoding='utf-8') as file_3:
	data3 = json.loads(file_3.read())

with open('news_data.json', 'w', encoding='utf-8') as filedata:
    rJson = json.dumps(data1 + data2 + data3, 
                        indent=4, 
                        sort_keys=True,
                        ensure_ascii=False)
    filedata.write(rJson)
import json

with open(("C:/Users/user/LYH/ModuleProject1/FacebookProject/data/%s_naver_news_test.json") % '코로나', encoding='utf-8') as file_1:
	data1 = json.loads(file_1.read())

with open(("C:/Users/user/LYH/ModuleProject1/FacebookProject/data/%s_naver_news_test.json") % '올림픽', encoding='utf-8') as file_2:
	data2 = json.loads(file_2.read())

with open(("C:/Users/user/LYH/ModuleProject1/FacebookProject/data/%s_naver_news_test.json") % '폭염', encoding='utf-8') as file_3:
	data3 = json.loads(file_3.read())

with open('C:/Users/user/LYH/ModuleProject1/FacebookProject/data/news_data_test.json', 'w', encoding='utf-8') as filedata:
    rJson = json.dumps(data1 + data2 + data3, 
                        indent=4, 
                        sort_keys=True,
                        ensure_ascii=False)
    filedata.write(rJson)
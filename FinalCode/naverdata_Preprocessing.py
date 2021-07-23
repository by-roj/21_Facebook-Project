import urllib.request
import datetime
import json

def GetDateChange(data, jsonResult):    # 데이터를 정제하는 부분
    resultTitle = data['title']
    resultDesc = data['description']
    resultOrgLink = data['originallink']
    naverLink = data['link']

    changeDate = datetime.datetime.strptime(data['pubDate'], 
                                            '%a, %d %b %Y %H:%M:%S +0900') # 표시 형식
    changeDateResult = changeDate.strftime('%Y-%m-%d %H:%M:%S')   # 표시 형식 변경 : 년-월-일 시:분:초

    jsonResult.append({'title':resultTitle,
                        'description':resultDesc,
                        'link':naverLink,
                        'originallink':resultOrgLink,
                        'pubDate':changeDateResult})

    return # 더이상 할 것이 없으니 호출한 함수로 돌아가기 - return 아래 코드가 있어도 실행되지 않음

def main(): # 정적 언어처럼 시작 함수 지정 가능
    keyword_list = ['코로나', '올림픽', '폭염', '비트코인', 'MZ세대', '주식', '거리두기', '집값', '델타', '학대']
    news_data = []

    for i in keyword_list:
        jsonDataResult = []
        with open(("C:/Users/user/LYH/ModuleProject1/FacebookProject/FinalCode/naverdata/%s_naver_news.json") % i, encoding='utf-8') as filedata:
            data = filedata.read()
            print(data['display'])
            # jsonfiledata = json.loads(filedata.read())

    #         for data in jsonfiledata['items']:  
    #             GetDateChange(data, jsonDataResult)
    #     news_data.append(jsonDataResult)

    # with open('naver_news_data.json', 'w', encoding='utf-8') as totaldata:
    #     rJson = json.dumps(news_data, 
    #                         indent=4, 
    #                         sort_keys=True,
    #                         ensure_ascii=False)
    #     totaldata.write(rJson)

    # print('naver_news_data.json 저장완료')

if __name__ == '__main__':  
    main()
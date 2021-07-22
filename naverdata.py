import urllib.request
import datetime
import json
# from config import *
# 실무에서는 최종 버전을 만들기 전까지는 개발 과정에서 혹시 나중에 사용될지 모르니 주석으로 우선 처리 → 최종에 삭제


client_id = "OhUkL9DQb6jD_IAmRmWD"
client_secret = "JMSDhP987z"

def get_request_url(url):   # 데이터 요청하여 가져오기 - 크롤러 작업
    req = urllib.request.Request(url)   # 검색 URL 경로 지정
    req.add_header("X-Naver-Client-Id", client_id)  # 경로 접근하기 위한 아이디 - naver에서 발급
    req.add_header("X-Naver-Client-Secret", client_secret)  # 경로 접근하기 위한 비밀번호 - naver에서 발급

    try:
        response = urllib.request.urlopen(req)  # URL을 통해 데이터 요청해서 결과 받음
        if response.getcode() == 200:   # 200 코드 번호면 성공. 400, 500은 Naver 문서에서 확인
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())  # 현재 시간
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s" % datetime.datetime.now(), url)
        return None

# 크롤러로 데이터로 가져오기 전 분류 / 인증 절차 등 사전 준비 작업
def GetNaverSearchResult(searchNode, searchText, pageStart, display):   # 분류 시작 / 검색 기준
    baseurl = "https://openapi.naver.com/v1/search/"    # Naver에서 필수로 지정한 URL
    nodedata = "%s.json" % searchNode   # 뉴스를 가져오는데 결과는 json 파일 형식
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(searchText), # 단어
                                                    pageStart,  # 검색 시작점
                                                    display)   # 검색 결과 레코드 수
    url = baseurl + nodedata + parameters   # 모든 것 합쳐서 URL 경로명 완성

    # 비정형(반정형)으로 가지고 온 초기 데이터(or 정형일 수도 있음)
    reqDataResult = get_request_url(url)    # 가져오기 위해서 URL 완성 후 처리를 위한 함수 호출
    # reqDataResult : Data Lake 저장

    if reqDataResult == None:   # 결과가 있는지 없는지 확인
        print("Data가 없습니다")
        return None
    else:
        return json.loads(reqDataResult)    # 데이터를 정형으로 변경
        

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
    jsonDataResult = []

    sNode = 'news'  # news / blog 항목을 선택(move)
    sText = '폭염'
    dCount = 100

    # 원시 데이터 가져옴(Data Lake에서 정형 데이터를 가져옴)
    jsonSearchResult = GetNaverSearchResult(sNode, sText, 1, dCount)

    # while ((jsonSearchResult != None) and (jsonSearchResult['display'] != 0)):  # 무한 루프 가능성 높음
    for data in jsonSearchResult['items']:  
        GetDateChange(data, jsonDataResult)

    with open(('%s_naver_%s.json') % (sText, sNode), 'w', encoding='utf-8') as filedata:
        rJson = json.dumps(jsonDataResult, 
                            indent=4, 
                            sort_keys=True,
                            ensure_ascii=False)
        filedata.write(rJson)

    print('%s_naver_%s.json 저장완료' % (sText, sNode))

if __name__ == '__main__':  
    main()

# __name__ : 내장 변수 / 글로벌 변수 - 파이썬에서 정한(예약한) 이미 있는 변수
# naverdata.py 일 경우 __name__ = naverdata (파일 이름)
# 이 파일 안에서 함수를 실행 : __main__ 값이 이미 정해져 있음(예약)
# 처음 실행하는 함수 지정
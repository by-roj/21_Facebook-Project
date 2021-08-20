from flask import Flask, jsonify, request # 서버 구현을 위한 Flask
from flask_restx  import Api, Resource #API 구현을 위한 API Import

app = Flask(__name__) # 매개변수(파라미터)로 App 패키지 이름을 지정
api = Api(app) # Flask 개체를 API 개체로 등록

@api.route('/<int:id>')
class HelloWorld(Resource):
    def get(self, id):  # Get 방식으로 데이터를 전송 : 메서스 오버라이딩
        data = '%d Hello World' % id
        return jsonify(data)

    def put(self):
        pass

    def delete(self):
        pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
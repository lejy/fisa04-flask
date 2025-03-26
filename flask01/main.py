
from flask import Flask

def create_app():
     app = Flask(__name__)

     from views import main_views
     app.register_blueprint(main_views.mbp)

     # URL과 FLASK코드를 매핑하는 Flask 데코레이터
     # @app.route처럼 애노테이션으로 URL을 매핑하는 함수를 라우팅 함수라고 부릅니다.
     @app.route('/')
     def hello():
          return f'Hello, {__name__}'

     @app.route('/yeonji')
     def hello_yeonji():
          return f'Hello, yeonji'
     
    
     return app
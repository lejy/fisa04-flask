
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
     app = Flask(__name__)
     app.config.from_object(config)

     # ORM을 적용
     db.init_app(app)
     migrate.init_app(app,db)

     from views import main_views,board_views
     app.register_blueprint(main_views.mbp)
     app.register_blueprint(board_views.cbp)
     

     # URL과 FLASK코드를 매핑하는 Flask 데코레이터
     # @app.route처럼 애노테이션으로 URL을 매핑하는 함수를 라우팅 함수라고 부릅니다.
     @app.route('/')
     def hello():
          return f'Hello, {__name__}'

     @app.route('/yeonji')
     def hello_yeonji():
          return f'Hello, yeonji'
     

    
     return app
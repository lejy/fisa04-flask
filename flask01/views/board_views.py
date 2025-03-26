from flask import Blueprint

# 특정 /main/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask의 기능
                # 코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로
cbp = Blueprint('collection', __name__, url_prefix='/collection')

#로컬5001/main
@cbp.route('/')
def hello4():
    return f'{__name__} 1'
@cbp.route('/no2')
def hello5():
    return f'{__name__} 2'
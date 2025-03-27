from flask import Blueprint
from ..models import Question,Answer

# 특정 /main/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask의 기능
                # 코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로
mbp = Blueprint('main', __name__, url_prefix='/first')

#로컬5001/main
@mbp.route('/')
def hello():
    return f'{__name__} hello'


@mbp.route('/<username>')
def print_string(username):
    return f'{__name__} {username} hello'

# path:변수명 : / 를 포함한 서브경로 전달
# float:변수명  : 플롯 전달
# int:변수명  : int 전달달
@mbp.route('/path/<path:subpath>')
def print_path(subpath):
    return f'{__name__} {subpath} hello'

@mbp.route('/상품/')
@mbp.route('/item/')
@mbp.route('/item/<itemname>')
@mbp.route('/item/<itemname>/<int:quantity>')
def print_itemname(itemname="기본값",quantity = 0):
    print(type(quantity))
    return f'{__name__} {itemname,quantity} hello'
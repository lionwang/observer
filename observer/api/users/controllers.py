from flask import request, g

from observer import app, db, auth
from observer.utils import response_util as responseUtil
from observer.utils import auth_util as authUtil
from observer.utils import encrypt_util as encryptUtil
from observer.api.users.model.user import User

@app.route('/api/v1/users/login', methods=['POST'])
def login():
    json_data = request.json
    username = json_data.get('username')
    password = json_data.get('password')
    if username == None or password == None:
        return responseUtil.error(50001, '用户名密码为空')
    user = User.query.filter_by(username=username).first()
    if user == None:
        return responseUtil.error(50002, '用户不存在')
    md5_password = encryptUtil.md5_encrypt(password, user.salt)
    if user.password != md5_password:
        return responseUtil.error(50003, '密码错误')
    return responseUtil.ok({'accessToken': str(user.generate_auth_token(), encoding = "utf-8")})

@app.route('/api/v1/users/info', methods=['POST', 'GET'])
@auth.login_required
def user_info():
    if None != g.user_id:
        user = User.query.get(g.user_id)
        return responseUtil.ok({'user': user.serialize()})
    return responseUtil.error(50004, '未知错误')

@app.route('/api/v1/users/info/<int:user_id>', methods=['POST', 'GET'])
@auth.login_required
def info(user_id):
    user = db.session.query(User).get(user_id)
    return responseUtil.ok({'user': user.serialize()})

@app.route('/api/v1/users/logout', methods=['POST', 'GET'])
@auth.login_required
def logout():
    return responseUtil.ok()

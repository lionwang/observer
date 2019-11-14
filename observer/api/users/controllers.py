from observer import app
from observer.utils import responseUtil
from flask import request

@app.route('/api/v1/users/login', methods=['POST'])
def login():
    return responseUtil.ok({'accessToken': 'admin-token'})

userList = [{
    'id': 0,
    'username': 'admin',
    'password': 'any',
    'name': 'Super Admin',
    'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
    'introduction': 'I am a super administrator',
    'email': 'admin@test.com',
    'phone': '1234567890',
    'roles': ['admin'],
}]

@app.route('/api/v1/users/info/<int:user_id>', methods=["POST, GET"])
def info():
    return responseUtil.ok({'user': userList[0]})

@app.route('/api/v1/users/logout/<int:user_id>', methods=['POST', 'GET'])
def logout():
    return responseUtil.ok()

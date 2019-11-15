from flask import g, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,  SignatureExpired, BadSignature

from observer import app, auth

@auth.verify_token
def verify_token(token):
    g.user_id = None
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return False  # valid token, but expired
    except BadSignature:
        return False  # invalid token
    if 'id' in data:
        g.user_id = data['id']
        return True
    return False

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 401
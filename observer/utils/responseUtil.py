from flask import jsonify

def ok(data = None, code = 20000):
    if data == None:
        ret_data = {'code': code}
    else:
        ret_data = {'code': code, 'data': data}
    return jsonify(ret_data)
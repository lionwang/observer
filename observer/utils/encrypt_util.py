from random import Random
import hashlib

def md5_encrypt(password, salt=''):
    return hashlib.md5((password + salt).encode("utf-8")).hexdigest()

# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length = 5):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    random = Random()
    for i in range(length):
        # 每次从chars中随机取一位  
        salt += chars[random.randint(0, len_chars)]
    return salt
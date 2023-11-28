from django.shortcuts import render
import random, base64, hashlib, string, binascii
from Crypto.Cipher import AES
from django.db import connection
import traceback,sys
from django.conf import settings
from common import sqls

# Create your views here.

secret_key = hashlib.sha256(b'key').digest()
iv = hashlib.md5(b'iv').digest()

# ランダムな6桁の数字の文字列を生成する
def ComRandomNum(n):
    num = '0123456789'
    return ''.join(random.choices(num, k=n))

def ComGetEncrypt(msg):
    # 文字列をbytesに変換
    raw_msg = base64.b64encode(msg.encode('utf-8'))
    # Cryptoを使うために16の倍数にする
    if len(raw_msg) % 16 != 0:
        b64_msg = raw_msg.decode('utf-8')
        for i in range(16 - (len(raw_msg) % 16)):
            b64_msg += '_'
    else :
        b64_msg = raw_msg.decode('utf-8')

    crypto = AES.new(secret_key, AES.MODE_CBC, iv)
    b64_msg_bytes = b64_msg.encode()
    ec_msg = crypto.encrypt(b64_msg_bytes)

    return ec_msg.hex()

def ComGetDecrypt(bytes_msg):

    str_to_hex = binascii.unhexlify(bytes_msg)
    crypto = AES.new(secret_key, AES.MODE_CBC, iv)

    b64_bytes = crypto.decrypt(str_to_hex)

    b64_msg = b64_bytes.decode("utf-8")
    raw_msg = b64_msg.split("_")[0]

    msg = base64.b64decode(raw_msg.encode("utf-8")).decode("utf-8")

    return msg

# SQLを叩いて、DBからデータを取得する関数
def ComGetQuery(query, args):

    try:
        cursor = connection.cursor()
        cursor.execute(query, args)

        columns = [col[0] for col in cursor.description]
        return dictfetchall(columns, cursor)
    
    except:
        return {
            "except_flag": True
        }
    
    finally:
        cursor.close()

# SQLで持ってきたデータを辞書型にする関数
def dictfetchall(columns, cursor):
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# cookieの値を取得する
def ComGetCookie(reqest,name):

    try:
        return ComGetDecrypt(reqest.COOKIES.get(name))
    
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.print_exc())
        print('Cookie is Not Set:{}'.format(name))
        return False

# cookieに値をセットする
def ComSetCookie(response,name,value,age):

    try:
        if age == 0:
            age = None
        
        response.set_cookie(
            name,
            ComGetEncrypt(str(value)),
            age,
        )

        return response
    
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.print_exc())
        print('Cookie is Not Set:{}/{}/{}'.format(name,value,age))
        return False

# セッションチェック
def ComSessionCheck(request):

    try:
        cookie_user_id = ComGetCookie(request,settings.LOGIN_USER_ID)

        if not cookie_user_id:
            return False
        
        query = sqls.GetUserIdByUserId()

        args = [
            cookie_user_id
        ]

        qdata = ComGetQuery(query,args)

        if "except_flag" in qdata:
            return False
        
        if not qdata:
            return False
        
        return True

    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.print_exc())
        return False
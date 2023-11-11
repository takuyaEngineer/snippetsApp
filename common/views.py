from django.shortcuts import render
import random, base64, hashlib, string, binascii
from Crypto.Cipher import AES
from django.db import connection

# Create your views here.

secret_key = hashlib.sha256(b'key').digest()
iv = hashlib.md5(b'iv').digest()

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

# SQLで持ってきたデータを辞書型にする関数
def dictfetchall(columns, cursor):
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
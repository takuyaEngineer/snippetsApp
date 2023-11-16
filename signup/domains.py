from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage
from django.conf import settings

from common import sqls
from common.views import ComGetQuery, ComSetCookie
from common.models import User

from signup.consts import *

import sys, traceback

# 入力された情報を元に、DBにユーザーを登録する。
def DomSignupCreateSave(params):

    context = {"try_flag": True, "msg": ""}

    try:
        query = sqls.GetUserByEmail()

        args = [
            params["email"]
        ]

        qdata = ComGetQuery(query, args)

        if type(qdata) == type({}):
            if qdata["except_flag"]:
                context["try_flag"] = "except"
                return context

        if qdata:
            context["try_flag"] = False
            context["msg"] = SIGNUP_MSG["user_already_exists"]
            return
        
        user = User()
        user.name = params["name"]
        user.email = params["email"]
        user.password = make_password(params["password"])
        user.save()

        return context
    
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        context["try_flag"] = "except"
        return context


# 入力された認証コードが正しいかどうか確認する。
def DomSignupAuthCompare(params):

    context = {"try_flag": True, "msg": ""}

    try:
        if params["cookie_auth_code"] != params["req_auth_code"]:
            context["try_flag"] = False
            context["msg"] = SIGNUP_MSG["auth_check_false"]
        
        return context
        
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        context["try_flag"] = "except"
        return context

# 入力されたメールアドレス宛てに認証コードを送信する。
def DomSignupEmailSend(response,params):

    context = {"try_flag": True, "msg": ""}

    try:
        query = sqls.GetUserByEmail()

        args = [
            params["email"]
        ]

        qdata = ComGetQuery(query,args)

        if type(qdata) == type({}):
            if qdata["except_flag"]:
                context["try_flag"] = "except"
                return context
        
        if qdata:
            # 既に登録済みの場合、ログインするように促すメールを送信する。
            subject = "登録済みのメールアドレスです。"
            message = """
            そのメールアドレスは既に登録済みです。ログイン画面からログインしてください。
            """
            from_email = "ngctky626@gmail.com"
            recipient_list = [params["email"]]
            email = EmailMessage(subject, message, from_email, recipient_list)
            email.send()
            return context
        
        # cookieに認証コードとメールアドレスをセットする
        ComSetCookie(response,settings.SIGNUP_AUTH_CODE,params["auth_code"],settings.COOKIE_AGE_1D)
        ComSetCookie(response,settings.SIGNUP_EMAIL,params["email"],settings.COOKIE_AGE_1D)

        # 認証コードを送信する
        subject = "会員登録　認証コードの送信"
        message = params["auth_code"]
        from_email = "ngctky626@gmail.com"
        recipient_list = [params["email"]]
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.send()

        return context
    
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        context["try_flag"] = "except"
        return context

from common import sqls
from common.views import ComGetQuery, ComSetCookie
from login.consts import LOGIN_MSG
from django.contrib.auth.hashers import check_password
from django.conf import settings

# DBからユーザーの情報を取得する
def DomGetUser(params):

    context = {"try_flag": True, "msg": ""}
    
    try:
        query = sqls.GetUserByEmail()
        args = [
            params["email"]
        ]
        qdata = ComGetQuery(query,args)

        print("qdata",qdata)

        if not qdata:
            context["try_flag"] = False
            context["msg"] = LOGIN_MSG["user_unregistered"]
            return context

        if "except_flag" in qdata:
            context["try_flag"] = False
            context["msg"] = LOGIN_MSG["user_unregistered"]
            return context
        
        if not check_password(params["password"], qdata[0]["password"]):
            context["try_flag"] = False
            context["msg"] = LOGIN_MSG["user_unregistered"]
            return context
        
        context["user"] = qdata[0]
        return context
    
    except:
        context["try_flag"] = "except"
        return context

# ログイン情報をcookieにセットする
def DomLoginCookieSave(response,params):

    context = {"try_flag": True, "msg": ""}

    try:
        ComSetCookie(response,settings.LOGIN_USER_ID,params["user_id"],settings.COOKIE_AGE_1D)

        return context
    
    except:
        context["try_flag"] = False
        return context
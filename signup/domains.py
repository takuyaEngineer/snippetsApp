from common import sqls
from common.views import ComGetQuery
from common.models import User
from signup.consts import *
from django.contrib.auth.hashers import make_password
import sys, traceback

def DomSignupCreateSave(context, params):

    query = sqls.MailDuplicationCheck()

    args = [
        params["email"]
    ]

    qdata = ComGetQuery(query, args)

    if qdata:
        context["msg"] = "そのメールアドレスは既に登録済みです。"
        context["try_flag"] = False
        return
    
    user = User()
    user.name = params["name"]
    user.email = params["email"]
    user.password = make_password(params["password"])
    user.save()

def DomSignupAuthCompare(context, params):

    try:
        if params["cookie_auth_code"] != params["req_auth_code"]:
            context["try_flag"] = False
            context["msg"] = SIGNUP_MSG["auth_check_false"]
        
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        context["try_flag"] = "except"
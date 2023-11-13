from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.domains import DomGetUser, DomLoginCookieSave
import json, sys, traceback

# ログインページを表示する
def LoginIndex(request):
    return render(request, 'login/index.html')

# ログインをする
def LoginCheck(request):
        
    context = {"try_flag": True, "msg": ""}

    try:
        response = HttpResponse(content_type="application/json", charset="utf-8", status=200)

        req_body_json = json.loads(request.body.decode('utf-8'))

        print(req_body_json["email"])

        # DBから一致するユーザーの情報を取得する
        return_value = DomGetUser(req_body_json)

        # DBに一致するユーザーが存在しなかった場合、falseを返す
        if not return_value["try_flag"]:
            context["try_flag"] = False
            context["msg"] = return_value["msg"]
            response.content = json.dumps(context)
            return response
                
        # ログインするユーザーの情報をcookieに保存する
        params = {
            "user_id": return_value["user"]["id"],
        }
        return_value = DomLoginCookieSave(response,params)
        if return_value["try_flag"] == False:
            context["try_flag"] = False
            response.content = json.dumps(context)
            return response

        response.content = json.dumps(context)
        return response

    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        print(request.POST)
        context["try_flag"] = "except"
        return context

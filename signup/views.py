from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf import settings

from common.views import ComRandomNum, ComGetDecrypt

from signup.domains import DomSignupCreateSave, DomSignupAuthCompare, DomSignupEmailSend

import json, sys, traceback


def SignupEmailCheck(request):
    return render(request, 'signup/email_check.html')


def SignupEmailsend(request):

    context = {"try_flag": True, "msg": ""}

    try:
        response = HttpResponse(content_type="application/json", charset="utf-8", status=200)

        # 認証コードになる6桁のランダムな文字列を生成
        auth_code = ComRandomNum(6)

        req_body_json = json.loads(request.body.decode('utf-8'))

        params = {
            "auth_code":auth_code,
            "email":req_body_json["email"]
        }

        return_value = DomSignupEmailSend(response,params)
        context["try_flag"] = return_value["try_flag"]

        response.content = json.dumps(context)

        return response

    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        print(request.POST)
        context["try_flag"] = "except"
        response.content = json.dumps(context)
        return response


def SignupAuthCheck(request):
    return render(request, 'signup/auth_check.html')


def SignupAuthSend(request):
    
    context = {"try_flag": True, "msg": ""}

    try:
        response = HttpResponse(content_type="application/json", charset="utf-8", status=200)

        req_body_json = json.loads(request.body.decode('utf-8'))

        params = {
            "cookie_auth_code": ComGetDecrypt(request.COOKIES.get(settings.SIGNUP_AUTH_CODE)),
            "req_auth_code": req_body_json["auth_code"]
        }

        return_value = DomSignupAuthCompare(params)
        context["try_flag"] = return_value["try_flag"]
        context["msg"] = return_value["msg"]

        response.content = json.dumps(context)

        return response

    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        print(request.POST)
        context["try_flag"] = "except"
        return context


def SignupNew(request):

    if request.META.get("HTTP_REFERER","") != "http://localhost:8000/signup/auth/check/":
        return HttpResponseRedirect(reverse("signup/email/check"))
    
    return render(request, 'signup/new.html')


def SignupCreate(request):
        
    context = {"try_flag": True, "msg": ""}

    try:
        if request.META.get("HTTP_REFERER","") != "http://localhost:8000/signup/new/":
            return HttpResponseRedirect(reverse("signup/email/check"))

        response = HttpResponse(content_type="application/json", charset="utf-8", status=200)

        req_body_json = json.loads(request.body.decode('utf-8'))

        params = {
            "name": req_body_json["name"],
            "email": ComGetDecrypt(request.COOKIES.get(settings.SIGNUP_EMAIL)),
            "password": req_body_json["password"],
        }

        return_value = DomSignupCreateSave(params)
        context["try_flag"] = return_value["try_flag"]
        context["msg"] = return_value["msg"]

        response.content = json.dumps(context)

        return response

    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        print(request.POST)
        context["try_flag"] = "except"
        return context

def SignupFin(request):

    return render(request, 'signup/fin.html')
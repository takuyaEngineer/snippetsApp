from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage
from common.views import ComGetEncrypt, ComRandomNum, ComGetDecrypt
from signup.domains import DomSignupCreateSave, DomSignupAuthCompare
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

        enc_auth_code = ComGetEncrypt(auth_code)
        enc_email = ComGetEncrypt(req_body_json["email"])

        response.set_cookie('auth_code', enc_auth_code)
        response.set_cookie('email', enc_email)

        # メールを送信する
        subject = "会員登録　認証コードの送信"
        message = auth_code
        from_email = "ngctky626@gmail.com"
        recipient_list = [req_body_json["email"]]
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.send()

        response.content = json.dumps(context)

        return response

    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        print(request.POST)
        return redirect("maintenance/except")


def SignupAuthCheck(request):
    return render(request, 'signup/auth_check.html')


def SignupAuthSend(request):
    
    context = {"try_flag": True, "msg": ""}

    try:
        response = HttpResponse(content_type="application/json", charset="utf-8", status=200)

        req_body_json = json.loads(request.body.decode('utf-8'))

        cookie_auth_code = ComGetDecrypt(request.COOKIES.get("auth_code"))
        req_auth_code = req_body_json["auth_code"]

        params = {
            "cookie_auth_code": cookie_auth_code,
            "req_auth_code": req_auth_code
        }

        DomSignupAuthCompare(context, params)

        response.content = json.dumps(context)

        return response

    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        print(request.POST)
        return redirect("maintenance/except")


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

        email = ComGetDecrypt(request.COOKIES.get("email"))
        req_body_json["email"] = email

        DomSignupCreateSave(context, req_body_json)

        response.content = json.dumps(context)

        return response

    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.format_exc())
        print(request.POST)
        return redirect("maintenance/except")

def SignupFin(request):

    return render(request, 'signup/fin.html')
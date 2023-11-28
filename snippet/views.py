from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

from snippet.forms import SnippetForm
from snippet.domains import DomSnippetCreate, DomGetSnippetList, DomGetSnippetDetail, DomUpdateSnippet, DomDeleteSnippet
from common.models import Snippet
from common.views import ComSessionCheck
from top.views import top
from maintenance.views import Except

import traceback,sys

def SnippetIndex(request):

    context = {"try_flag": True, "msg": ""}

    # セッションチェック
    return_value = ComSessionCheck(request)
    if not return_value:
        return redirect(top)
    
    # スニペット一覧を取得
    return_value = DomGetSnippetList()
    if return_value["try_flag"] == True:
        context["snippet_list"] = return_value["snippet_list"]

    return render(request,"snippet/index.html",context)

def SnippetNew(request):

    return render(request, "snippet/new.html")

def SnippetCreate(request):

    params = {
        "title": request.POST.get("title"),
        "description": request.POST.get("description"),
        "code": request.POST.get("code"),
    }

    return_value = DomSnippetCreate(params)
    if not return_value:
        redirect(Except)

    return render(request, "snippet/index.html")


def SnippetDetail(request, snippet_id):

    context = {"try_flag": True, "msg": ""}

    try:
        # スニペットを取得
        params = {
            "snippet_id": snippet_id
        }
        return_value = DomGetSnippetDetail(params)
        if return_value["try_flag"] == True:
            context["snippet"] = return_value["snippet"]

        return render(request, "snippet/detail.html", context)
    
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.print_exc())
        return redirect(Except)


def SnippetEdit(request, snippet_id):

    context = {"try_flag": True, "msg": ""}

    try:
        # スニペットを取得
        params = {
            "snippet_id": snippet_id
        }
        return_value = DomGetSnippetDetail(params)
        if return_value["try_flag"] == True:
            context["snippet"] = return_value["snippet"]

        return render(request, "snippet/edit.html", context)
    
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.print_exc())
        return redirect(Except)


def SnippetUpdate(request, snippet_id):

    context = {"try_flag": True, "msg": ""}

    try:
        # スニペットを更新
        params = {
            "id": snippet_id,
            "title": request.POST.get("title"),
            "description": request.POST.get("description"),
            "code": request.POST.get("code"),
        }
        return_value = DomUpdateSnippet(params)
        if return_value["try_flag"] == False:
            print(return_value["msg"])
            return redirect(Except)
        
        return redirect(SnippetDetail,snippet_id)
    
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.print_exc())
        return redirect(Except)


def SnippetDelete(request, snippet_id):

    context = {"try_flag": True, "msg": ""}

    try:
        # スニペットを削除
        params = {
            "id": snippet_id,
        }
        return_value = DomDeleteSnippet(params)
        if return_value["try_flag"] == False:
            print(return_value["msg"])
            return redirect(Except)
        
        return redirect(SnippetIndex)
    
    except:
        print(sys._getframe().f_code.co_name)
        print(traceback.print_exc())
        return redirect(Except)
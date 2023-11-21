from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

from snippet.forms import SnippetForm
from snippet.domains import DomSnippetCreate
from common.models import Snippet
from common.views import ComSessionCheck
from top.views import top
from maintenance.views import Except

import json

def SnippetIndex(request):

    return_value = ComSessionCheck(request)
    print(return_value)
    if not return_value:
        return redirect(top)

    return render(request,"snippet/index.html")

def SnippetNew(request):

    return render(request, "snippet/new.html")

def snippetCreate(request):

    params = {
        "title": request.POST.get("title"),
        "description": request.POST.get("description"),
        "code": request.POST.get("code"),
    }

    return_value = DomSnippetCreate(params)
    if not return_value:
        redirect(Except)

    return render(request, "snippet/index.html")

def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("このスニペットの編集は許可されていません。")
    
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect(snippet_detail, snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippet/snippet_edit.html', {'form': form})

def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    context = {"snippet": snippet}
    return render(request, "snippet/detail.html", context)

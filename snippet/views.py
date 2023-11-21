# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

from snippet.forms import SnippetForm
from common.models import Snippet
from common.views import ComSessionCheck
from top.views import top

def SnippetIndex(request):

    return_value = ComSessionCheck(request)
    print(return_value)
    if not return_value:
        return redirect(top)

    return render(request,"snippet/index.html")

def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, "snippet/snippet_new.html", {"form": form})

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

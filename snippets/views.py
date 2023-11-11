# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.core.mail import send_mail, EmailMessage

from snippets.forms import SnippetForm
from common.models import Snippet

# Create your views here.

def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}

    # """題名"""
    # subject = "題名"
    # """本文"""
    # message = "本文です\nこんにちは。メールを送信しました"
    # """送信元メールアドレス"""
    # from_email = "information@myproject"
    # """宛先メールアドレス"""
    # recipient_list = [
    #     "ngctky626@gmail.com"
    # ]

    subject = "テストメール"
    message = "テストメールです。"
    from_email = "ngctky626@gmail.com"
    recipient_list = ["ngctky626@gmail.com"]
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.send()

    # send_mail(subject, message, from_email, recipient_list)
    return render(request, "snippets/top.html", context)

# @login_required
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
    return render(request, "snippets/snippet_new.html", {"form": form})

# @login_required
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
    return render(request, 'snippets/snippet_edit.html', {'form': form})

def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    context = {"snippet": snippet}
    return render(request, "snippets/detail.html", context)

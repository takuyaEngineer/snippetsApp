from django.db import models

class Snippet(models.Model):
    title = models.CharField('タイトル', max_length=128)
    code = models.TextField('コード', blank=True)
    description = models.TextField('説明', blank=True)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = 'snippet'

class Comment(models.Model):
    text = models.TextField("本文", blank=False)
    commented_to = models.ForeignKey(Snippet, verbose_name="スニペット", on_delete=models.CASCADE)

    class Meta:
        db_table = "comment"

class Tag(models.Model):
    name = models.TextField("タグ名", max_length=32)
    snippets = models.ManyToManyField(Snippet, related_name='tags', related_query_name='tag')

    class Meta:
        db_table = "tag"

class User(models.Model):
    id = models.BigAutoField(null=False,primary_key=True)
    name = models.TextField(blank=True,null=True,default='')
    email = models.TextField(blank=True,null=True,default='')
    password = models.TextField(blank=True,null=True,default='')
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    created_at = models.DateTimeField(null=True,auto_now=True)
    active_flag = models.BooleanField(default=True)

    class Meta:
        db_table = "user"

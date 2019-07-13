import uuid

from django.db import models


class Scene(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # on_deleteとは参照するオブジェクトが削除されたときに、
    # それと紐づけられたオブジェクトも一緒に削除するのか、
    # それともそのオブジェクトは残しておくのかを設定するもの
    # https://djangobrothers.com/blogs/on_delete/
    # user情報が不用意に消えるのを防ぐためにPROTECTを使用
    user_id = models.ForeignKey('user.User', on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    # シーンサイズの縦横の大きさ
    width = models.IntegerField()
    higth = models.IntegerField()
    # シーンの縦横のグリッド数
    columm_count = models.IntegerField()
    line_count = models.IntegerField()
    # 作成日と更新日を自動取得
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

import uuid

from uuid import UUID

from django.db import models


class Scene(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # on_deleteとは参照するオブジェクトが削除されたときに、
    # それと紐づけられたオブジェクトも一緒に削除するのか、
    # それともそのオブジェクトは残しておくのかを設定するもの
    # https://djangobrothers.com/blogs/on_delete/
    # user情報が不用意に消えるのを防ぐためにPROTECTを使用
    # db_columnでDBの列名をuser_idに明示的に変更
    user_id = models.ForeignKey('user.User', on_delete=models.PROTECT, db_column='user_id')
    name = models.CharField(max_length=30)
    # シーンサイズの縦横の大きさ
    width = models.IntegerField()
    hight = models.IntegerField()
    # シーンの縦横のグリッド数
    columm_count = models.IntegerField()
    line_count = models.IntegerField()
    # 作成日と更新日を自動取得
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def set_user_id(self, user):
        self.user_id = user

    def set_name(self, name):
        self.name = name

    def set_width(self, width):
        self.width = width

    def set_hight(self, hight):
        self.hight = hight

    def set_column_count(self, columm_count):
        self.columm_count = columm_count

    def set_line_count(self, line_count):
        self.line_count = line_count

    def get_scene_data(self, scene_id):
        '''
        受け取ったシーンIDに対応するクエリセットを返す
        対応するデータがない場合や受け取ったシーンIDがUUID4ではない場合は何も返さない
        '''
        if self.validate_uuid4(scene_id):
            return Scene.objects.filter(id=scene_id)

    def validate_uuid4(self, string):
        '''
        受け取った文字列がUUID4か確認
        '''
        try:
            UUID(string, version=4)
        except ValueError:
            return False
        return True

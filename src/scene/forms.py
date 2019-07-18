from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from scene.models import Scene


class SceneConfigForm(forms.ModelForm):
    name = forms.CharField(max_length=30, help_text='シーン名を入力してください')
    # 下記サイトを参考に最大値は幅を8192、高さを4320。最小値は幅128、高さ96。
    # http://www.quel.jp/etc/monitor-size/
    width = forms.IntegerField(validators=[MinValueValidator(128),
                               MaxValueValidator(8192)],
                               help_text='シーンの幅を入力してください')
    height = forms.IntegerField(validators=[MinValueValidator(96),
                                MaxValueValidator(4320)],
                                help_text='シーンの高さを入力してください')
    # 試験的に最大横グリッド数を100、縦グリッド数を100。
    column_count = forms.IntegerField(validators=[MinValueValidator(1),
                                      MaxValueValidator(100)],
                                      help_text='横のグリッド数を入力してください')
    line_count = forms.IntegerField(validators=[MinValueValidator(1),
                                    MaxValueValidator(100)],
                                    help_text='縦のグリッド数を入力してください')

    class Meta():
        model = Scene
        fields = ('name', 'width', 'height', 'column_count', 'line_count')

    def save(self, commit=True):
        user = self.instance
        scene = Scene()
        scene.set_user_id(user)
        scene.set_name(self.cleaned_data.get('name'))
        scene.set_width(self.cleaned_data.get('width'))
        scene.set_height(self.cleaned_data.get('height'))
        scene.set_column_count(self.cleaned_data.get('column_count'))
        scene.set_line_count(self.cleaned_data.get('line_count'))
        if commit:
            scene.save()
        return scene

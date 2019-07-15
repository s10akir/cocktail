from django import forms

from scene.models.scene import Scene


class SceneConfigForm(forms.ModelForm):
    name = forms.CharField(max_length=30, help_text='シーン名を入力してください')
    width = forms.IntegerField(help_text='シーンサイズの横の大きさを入力してください')
    hight = forms.IntegerField(help_text='シーンサイズの縦の大きさを入力してください')
    column_count = forms.IntegerField(help_text='横のグリッド数を入力してください')
    line_count = forms.IntegerField(help_text='縦のグリッド数を入力してください')

    class Meta():
        model = Scene
        fields = ('name', 'width', 'hight', 'column_count', 'line_count')

    def save(self, commit=True):
        user = self.instance
        scene = Scene()
        scene.set_user_id(user)
        scene.set_name(self.cleaned_data.get('name'))
        scene.set_width(self.cleaned_data.get('width'))
        scene.set_hight(self.cleaned_data.get('hight'))
        scene.set_column_count(self.cleaned_data.get('column_count'))
        scene.set_line_count(self.cleaned_data.get('line_count'))
        if commit:
            scene.save()
        return scene

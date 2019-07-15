from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Scene


@login_required
def showSceneData(request):
    if 'id' in request.GET:
        scene_id = request.GET.get('id')    # GET時のクエリ文字列のidからシーンIDを取得
        scene = Scene()
        scene_data = scene.get_scene_data(scene_id)

        if scene_data is not None:
            data = {'scene_data': scene_data}
            return render(request, 'show-scene-data.html', data)

    return render(request, 'show-scene-data.html')

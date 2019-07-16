from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from scene.forms import SceneConfigForm
from scene.models import Scene
from scene.models import SizeTemplate


@login_required
def configure_scene(request):
    if request.method == 'POST':
        form = SceneConfigForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SceneConfigForm()
    return render(request, 'scene-configure.html', {'form': form})


@login_required
def show_size_templates(request):
    size_template = SizeTemplate()
    templates = size_template.get_size_templates()
    templates_data = {'templates': templates}
    return render(request, 'show-size-templates.html', templates_data)


@login_required
def show_scene_data(request):
    if 'id' in request.GET:
        scene_id = request.GET.get('id')    # GET時のクエリ文字列のidからシーンIDを取得
        scene = Scene()
        scene_data = scene.get_scene_data(scene_id)

        if scene_data is not None:
            data = {'scene_data': scene_data}
            return render(request, 'show-scene-data.html', data)

    return render(request, 'show-scene-data.html')

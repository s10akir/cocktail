from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from scene.forms import SceneConfigForm
from scene.models import Scene, SizeTemplate


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
    templates = SizeTemplate.objects.all()
    templates_data = {'templates': templates}
    return render(request, 'show-size-templates.html', templates_data)


@login_required
def show_scene_data(request):
    if 'id' in request.GET:
        # GET時のクエリ文字列のidからシーンIDを取得
        scene_id = request.GET.get('id')
        user_id = request.user.id
        if scene_id is not None:
            scene = Scene()
            scene_data, error = scene.get_scene_data(scene_id, user_id)
            data = {
                'scene_data': scene_data,
                'error': error
            }
            return render(request, 'show-scene-data.html', data)

    return render(request, 'show-scene-data.html')

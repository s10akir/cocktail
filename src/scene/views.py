import json

from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import redirect, render, render_to_response

from cocktail.settings import BASE_DIR

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


def api_module(request, moduleName):
    f = open(BASE_DIR + '/modules/' + moduleName + '.js', "rb")
    module = File(f)
    return HttpResponse(content=module, content_type='application/javascript')


def scene_editor(request):
    return render(request, 'scene-editor.html')


def api_save_module(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        json_data = json.loads(json_str)
        for data in json_data:
            print(data)
        # return HttpResponseServerError()
        return HttpResponse(status=204)

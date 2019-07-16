from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from scene.forms import SceneConfigForm


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

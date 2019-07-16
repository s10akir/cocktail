from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from scene.models import SizeTemplate


@login_required
def show_size_templates(request):
    size_template = SizeTemplate()
    templates = size_template.get_size_templates()
    templates_data = {'templates': templates}
    return render(request, 'show-size-templates.html', templates_data)

from django.shortcuts import render

from .models import SizeTemplate


def showSizeTemplates(request):
    size_template = SizeTemplate()
    templates = size_template.get_size_templates()
    data = {'templates': templates}
    return render(request, 'show-size-templates.html', data)

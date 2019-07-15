from django.shortcuts import render


def showSizeTemplates(request):
    return render(request, 'show-size-templates.html')

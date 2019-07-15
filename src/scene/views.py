from django.shortcuts import render


def showSceneData(request):
    return render(request, 'show-scene-data.html')

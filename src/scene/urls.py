from django.urls import path

from . import views


app_name = 'scene'

urlpatterns = [
    path('show-scene-data/', views.showSceneData, name='show-scene-data'),
]

from django.urls import path

from . import views


app_name = 'scene'

urlpatterns = [
    path('scene-configure/', views.configure_scene, name='scene-configure')
]

from django.urls import path

from scene import views


app_name = 'scene'

urlpatterns = [
    path('scene-configure/', views.configure_scene, name='scene-configure')
]

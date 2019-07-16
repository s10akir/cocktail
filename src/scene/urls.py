from django.urls import path

from scene import views


app_name = 'scene'

urlpatterns = [
    path(
        'show-size-templates/',
        views.show_size_templates,
        name='show-size-templates'
    ),
    path('show-scene-data/', views.show_scene_data, name='show-scene-data'),
]

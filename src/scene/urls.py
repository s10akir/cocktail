from django.urls import path

from scene import views


app_name = 'scene'

urlpatterns = [
    path('scene-configure/', views.configure_scene, name='scene-configure'),
    path('show-size-templates/',
         views.show_size_templates,
         name='show-size-templates'),
    path('show-scene-data/', views.show_scene_data, name='show-scene-data'),
    path('scene-editor/', views.scene_editor, name='scene-editor'),
    path('api/module/<str:moduleName>', views.api_module, name='api-module'),
]

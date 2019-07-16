from django.urls import path

from scene import views


app_name = 'scene'

urlpatterns = [
    path(
        'show-size-templates/',
        views.show_size_templates,
        name='show-size-templates'
    ),
]

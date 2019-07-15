from django.urls import path

from . import views


app_name = 'scene'

urlpatterns = [
    path(
        'show-size-templates/',
        views.showSizeTemplates,
        name='show-size-templates'
    ),
]

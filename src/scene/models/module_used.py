from uuid import uuid4

from django.db import models

from scene.models import Scene


class Module_used(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    scene_id = models.ForeignKey('scene.Scene',
                                 on_delete=models.PROTECT,
                                 db_column='scene_id')
    module_id = models.CharField(max_length=10)
    row = models.CharField(max_length=10)
    column = models.CharField(max_length=10)
    grid_width = models.CharField(max_length=10)
    grid_height = models.CharField(max_length=10)
    data = models.CharField(max_length=512, null=True)

    def module_save(self, data):
        sceneId = Scene.objects.only('id').filter(id=data.get('sceneId'))
        Module_used.objects.create(
            scene_id=sceneId[0],
            id=data.get('id'),
            module_id=data.get('module'),
            row=data.get('top'),
            column=data.get('left'),
            grid_width=data.get('width'),
            grid_height=data.get('height'),
            data=data.get('data'),
        )
        return 204

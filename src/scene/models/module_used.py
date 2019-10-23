from uuid import uuid4

from django.db import models


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
    data = models.CharField(max_length=512)

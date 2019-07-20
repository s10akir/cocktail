from django.db import models


class SizeTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    width = models.IntegerField()
    height = models.IntegerField()

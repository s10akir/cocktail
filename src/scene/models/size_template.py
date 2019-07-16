from django.db import models


class SizeTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    width = models.IntegerField()
    height = models.IntegerField()

    def get_size_templates(self):
        '''
        SizeTemplateから全件取得する
        '''
        return SizeTemplate.objects.all()

from django.db import models

# Create your models here.
#ORM相关的东西只能写在这，写在别的地方Django找不到


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30)
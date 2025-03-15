from django.db import models

# Create your models here.

class CrudDB(models.Model):
    UserName=models.CharField(max_length=55)

    def __str__(self):
        return self.UserName
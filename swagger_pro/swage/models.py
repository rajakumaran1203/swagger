from uuid import uuid4

from django.db import models

# Create your models here.
class stu(models.Model):
    id = models.UUIDField(default=uuid4,primary_key=True,unique=True)
    name=models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    job = models.JSONField()
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
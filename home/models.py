from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=20)
    body=models.TextField(max_length=50)
    isDone=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.title
    
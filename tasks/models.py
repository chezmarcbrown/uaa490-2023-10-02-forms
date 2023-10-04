from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    priority = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title



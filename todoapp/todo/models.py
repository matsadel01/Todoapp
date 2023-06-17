from django.db import models
from django.apps import apps

app = apps.get_app_config('todo')

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        app_label = app.name

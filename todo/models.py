from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()
        
    def __str__(self) -> str:
        return self.name
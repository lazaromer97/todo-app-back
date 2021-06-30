from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(verbose_name='Name', max_length=120, unique=True)
    description = models.TextField(verbose_name='Description')
    completed = models.BooleanField(verbose_name='Completed', default=False)

    class Meta:
        db_table = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name

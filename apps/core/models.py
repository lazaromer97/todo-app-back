from django.db import models

# Create your models here.


class Task(models.Model):
    text = models.CharField(verbose_name='Text', max_length=120, unique=True)
    completed = models.BooleanField(verbose_name='Completed', default=False)

    class Meta:
        db_table = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.text


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Text', max_length=255)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text

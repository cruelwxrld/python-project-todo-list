from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    description = models.TextField(verbose_name="description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    completed = models.BooleanField(default=False, verbose_name='completed')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['created_at']

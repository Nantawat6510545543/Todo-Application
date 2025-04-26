from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/todo_photos/<user_id>/<filename>
    return f'todo_photos/{instance.user.id}/{filename}'


class Todo(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.title

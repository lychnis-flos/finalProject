from django.db import models
from django.utils import timezone

CATEGORY_CHOICES = [
    ('本', '本'),
    ('映画', '映画'),
    ('音楽', '音楽'),
]

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

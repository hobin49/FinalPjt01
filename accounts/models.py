from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class User(AbstractUser):
    profile = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(100, 100)],
                                format='JPEG',
                                options={'quality': 50})
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')
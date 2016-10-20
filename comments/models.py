from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from messenger.models import Post
# Create your models here.
class Comment(models.Model):
	user =models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	post =models.ForeignKey(Post)
	content =models.TextField()
	timestamp =models.DateTimeField(auto_now_add=True)

def __str__(self):
	return self.user.username
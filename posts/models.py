from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	def __srt__(self):
		return self.title
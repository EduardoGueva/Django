#-*-coding:utf-8-*-

from django.db import models

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=250)
	body=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title
from django.db import models


class Notepad(models.Model):
	title = models.CharField(max_length=99)
	description = models.TextField(blank=True)
	timestamp = models.DateField(auto_now_add=True)


	class Meta:
		ordering = ['title']  # configure this later . Not working 


	def __str__(self):
		return self.title +  ' | ' +   str(self.timestamp)

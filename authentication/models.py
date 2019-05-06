from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=300)
	location = models.CharField(max_length=99)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')


	def __str__(self):
		return f'{self.user.username} Profile'


	def save(self):
		super().save()


		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			new_img = (300, 300)
			img.thumbnail(new_img)
			img.save(self.image.path)



	
from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()

	def __str__(self):
		return ("%s - %s - %s - %s")  % (self.name,self.description,self.opening_time,self.closing_time)
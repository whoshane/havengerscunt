from django.db import models

class Team(models.Model):
	id = models.AutoField(primary_key=True)
	number = models.IntegerField(default=0, unique=True)
	name = models.CharField(max_length=200)
	score = models.IntegerField(default=0)
	items = models.ManyToManyField('Item', null=True,blank=True)

	def __unicode__(self):
		return self.name

class Item(models.Model):
	id = models.AutoField(primary_key=True)
	description = models.CharField(max_length=1000)
	number = models.IntegerField(default=0)
	score = models.IntegerField(default=0)

	def __unicode__(self):
		return self.description

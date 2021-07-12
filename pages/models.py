from django.db import models

# Create your models here.
class Team(models.Model):
	lastname         = models.CharField(max_length=100, verbose_name='Nom')
	firstname        = models.CharField(max_length=100, verbose_name='Prénom')
	designation      = models.CharField(max_length=100, verbose_name='Responsabilité')
	photo            = models.ImageField(upload_to='photos/%Y/%m/%d')
	facebook_link    = models.URLField(max_length=200, verbose_name = 'Facebook')
	twitter_link     = models.URLField(max_length=200, verbose_name = 'Twitter')
	google_link      = models.URLField(max_length=200, verbose_name = 'Google Plus')
	created_date     = models.DateTimeField(auto_now_add=True, verbose_name='Date creation')


	class Meta:
		verbose_name = 'Equipe'
		verbose_name_plural = 'Equipes'

	def __str__(self):
		return self.firstname
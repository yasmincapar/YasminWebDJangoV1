#from tabnanny import verbose
from django.db import models
from django.utils import timezone

class PlayerModel(models.Model):

    class Meta:
        verbose_name='Player'
        verbose_name_plural='Players'


    title= models.CharField(max_length=200,verbose_name='Player id')#char for title in admin page
    content=models.TextField(verbose_name='name and surname')#text for content 
    created_date = models.DateTimeField(default=timezone.now,verbose_name='time created')
    published_date = models.DateTimeField(blank=True, null=True,verbose_name='Yayınlanma Tarihi')

# Create your models here.
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
        #will only show the title

    #django is a framework of python not an API


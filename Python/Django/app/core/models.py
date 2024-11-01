from django.db import models

class Core(models.Model):
    firstname = models.CharField(max_length=200,blank=False,db_comment='This is your first name')
    lastname = models.CharField(max_length=200,blank=False,db_comment='This is your first name')
    email = models.CharField(max_length=200,blank=True)
    user_id = models.IntegerField(primary_key=True)

# Create your models here.

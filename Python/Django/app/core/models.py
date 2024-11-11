from django.db import models

class Core(models.Model):
    firstname = models.CharField(max_length=200,blank=False,db_comment='This is your first name')
    lastname = models.CharField(max_length=200,blank=False,db_comment='This is your first name')
    email = models.CharField(max_length=200,blank=True)
    user_id = models.IntegerField(primary_key=True)
    
# this will print firstname and lastname in core model os 
    # def __str__(self):
        # return f"{self.firstname} {self.lastname}"

# Create your models here.
class Detail(models.Model):

    core = models.ForeignKey(Core, on_delete=models.CASCADE, related_name='details')
    address = models.CharField(max_length=200,blank=True)
    Phone_number = models.IntegerField(blank=True,null=True)


class Working_Experience(models.Model):
    working_sector =  models.CharField(max_length=200,blank=False)
    

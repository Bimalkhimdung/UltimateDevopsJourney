# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

class User(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return self.username

class UserLegalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='legal_info')
    pan_number = models.CharField(max_length=16)
    cit_number = models.CharField(max_length=12)
    pf_number = models.CharField(max_length=16)
    citizenship_number = models.CharField(max_length=16)
    ssfid = models.CharField(max_length=16)
    
    def __str__(self):
        return f"Legal Info - {self.user.username}"

class UserContactDetail(models.Model):
    CONTACT_CHOICES = [
        ('Spouse', 'Spouse'),
        ('Parent', 'Parent'),
        ('Sibling', 'Sibling'),
        ('Friend', 'Friend'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_details')
    slug = models.SlugField(unique=True)
    number = models.CharField(max_length=20)
    contact_of = models.CharField(max_length=10, choices=CONTACT_CHOICES)
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Bank(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    acronym = models.CharField(max_length=10)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class UserBank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_accounts')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.bank.name}"
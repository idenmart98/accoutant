from django.db import models

# Create your models here.
class Profile(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    uid = models.CharField(max_length=50)
    
    def __str__(self):
        return self.login
    
    
class Category(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Note(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name='notes')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name='notes')
    
    def __str__(self):
        return self.name
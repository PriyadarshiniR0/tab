from django.db import models

# Create your models here.
class Country(models.Model):
    cno=models.IntegerField()
    cname=models.CharField(max_length=30,primary_key=True)
    def __str__(self):
        return self.cname

class Capital(models.Model):
    capname=models.CharField(max_length=30,primary_key=True)
    capno=models.IntegerField()
    cname=models.OneToOneField(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.capname


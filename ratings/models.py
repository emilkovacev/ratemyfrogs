from django.db import models

class Frog(models.Model):
    frog = models.URLField(max_length=1000)
    
    def __str__(self):
        return str(self.frog)

class User(models.Model):
    userid = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.userid)

class FrogRating(models.Model):
    frog = models.ManyToManyField(Frog)
    ratingaverage = models.DecimalField(max_digits=15, decimal_places=10)
    
    def __str__(self):
        return str(self.frog)

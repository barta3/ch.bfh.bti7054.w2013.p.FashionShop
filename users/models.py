from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    dateOfBirth = models.DateField('Birthday')
    
    def __unicode__(self):
        return self.firstName + ", " + self.email
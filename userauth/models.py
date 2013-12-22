from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    address = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
    town = models.CharField(max_length=20)

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password1','password2',
                  'first_name', 'last_name', 'email', 'address', 'zip', 'town']
        
    def save(self, commit=True):
        customer = super(UserCreationForm, self).save(commit=False)
        customer.set_password(self.cleaned_data["password1"])
        customer.save()
         
        return customer
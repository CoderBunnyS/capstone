from django.db import models
from django.urls import reverse


# Create your models here.

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def childAge(value):
    if value >6:
        raise ValidationError(
            _('Your child must be under 6 years old. %(value)s is too old'),
            params={'value': value},
        )


class Profile(models.Model):
    childname = models.CharField(max_length=100, default='')
    parentname = models.CharField(max_length=100, default='')
    age = models.PositiveIntegerField(validators=[childAge])
    dob = models.CharField(max_length=10, default='') 
    phonenum = models.CharField(max_length=10, default='') 
    email = models.EmailField(max_length=254, unique=True, default='')
    allergies = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.childname

class User(models.Model):
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    role = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username
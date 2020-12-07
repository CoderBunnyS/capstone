from django.db import models
import datetime 

# Create your models here.

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# def childAge(value):
#     if value >6:
#         raise ValidationError(
#             _('Your child must be under 6 years old. %(value)s is too old'),
#             params={'value': value},
#         )


class Profile(models.Model):
    
    childname = models.CharField(max_length=100)
    parentname = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[childAge])
    dob = models.DateField(max_length=10) 
    phonenum = models.CharField(max_length=10) 
    email = models.EmailField(max_length=254, unique=True)
    allergies = models.CharField(max_length=100)

    def __str__(self):
        return self.childname
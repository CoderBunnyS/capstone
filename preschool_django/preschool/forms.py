from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('childname', 'parentname', 'age', 'dob', 'phonenum', 'email', 'allergies')



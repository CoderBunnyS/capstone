from django import forms
from .models import Profile, User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('childname', 'parentname', 'age', 'dob', 'phonenum', 'email', 'allergies')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')



from .models import Profile, User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import ProfileForm, UserForm

from rest_framework import generics
from rest_framework import permissions

staff_logged_in = False
# Create your views here.

class ProfileList(View):
    def get(self, request):
        profiles = Profile.objects.all()
        return render(request, 'preschool/profile_list.html', {'profiles': profiles})

# class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
    

def profile_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'preschool/profile_detail.html', {'profile': profile})


class ProfileCreate(View):
    form_class = ProfileForm
    template_name = 'preschool/profile_form.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if(form.is_valid()):
            profile = form.save()
            return redirect('profile_detail', pk=profile.pk)
            return render(request, 'preschool/profile_form.html', {'form':form})


def profile_edit(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'preschool/profile_form.html', {'form': form})

def profile_delete(request, pk):
    Profile.objects.get(id=pk).delete()
    return redirect('profile_list')

class Home(View):
    def get(self, request):
        # staff_logged_in = request.session.get('staff_logged_in', False)
        staff_logged_in = False
        return render(request, 'preschool/home.html', {'staff_logged_in': staff_logged_in})

class Contact(View):
    def get(self, request):
        return render(request, 'preschool/contact.html')

class Staff(View):
    def get(self, request):
        return render(request, 'preschool/staff.html')




class Login(View):
    form_class = UserForm
    template_name = 'preschool/login.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # form = UserForm(request.POST)
        # if(form.is_valid()):
            # user = form.save()
            # request.session['staff_logged_in'] = True
            staff_logged_in = True
            return render('/')
            

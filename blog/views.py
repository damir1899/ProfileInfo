from django.shortcuts import render
from .models import Profile
from .admin import ProfileAdmin

def profile(request):
    all_data = Profile.objects.all()
    
    return render(request, 'blog/profile.html', {'context': all_data})

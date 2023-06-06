from django.shortcuts import render, redirect
from .models import Contact


def index(request):
    all_data = Contact.objects.all()
    
    return render(request, 'home/index.html', {'context': all_data})


def add_index(request):
    
    if request.method == 'POST':
        if 'post_img' in request.FILES:
            post_img = request.FILES['post_img']
            post_first = request.POST.get('post_first')
            post_last = request.POST.get('post_last')
            post_phone = request.POST.get('post_phone')
            post_email = request.POST.get('post_email')
            
            add = Contact(image = post_img,
                            first_name = post_first,
                            last_name = post_last,
                            email = post_email,
                            phone = post_phone)
            add.save()
            
            return redirect('/')
    
    return render(request, 'blog/index.html')
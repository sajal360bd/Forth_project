from django.shortcuts import render,redirect
from .form import *
from django.contrib import messages

from .models import *

# Create your views here.

def index(request):
    p = Profile.objects.all()
    pp = Profile_p.objects.all()
    p_2 = Profile_2.objects.all()
    p_3 = Profile_3.objects.all()
    p_4 = Profile_4.objects.all()
    p_5 = Profile_5.objects.all()
    p_6 = Profile_6.objects.all()
    p_7 = Profile_7.objects.all()
    p_8 = Profile_8.objects.all()
    
    h = home.objects.all()

    context = {
        'p':p,
        'pp':pp,
        'p_2':p_2,
        'p_3':p_3,
        'p_4':p_4,
        'p_5':p_5,
        'p_6':p_6,
        'p_7':p_7,
        'p_8':p_8,
        'h':h

        
    }
    return render(request, 'main_app/index.html', context)

def about(request):
    A = About_1.objects.all()
    A_1 = About_2.objects.all()

    context = {
        'A':A,
        'A_1':A_1,
    }
    return render(request, 'main_app/about.html',context)

def contact(request):
    form = Contact_f(request.POST)
    print(request.POST)
    if request.method == 'POST':
        form = Contact_f(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('/')
        else:
            form = Contact_f()
            return render(request, 'main_app/contact.html')
    context = {
        'form': form,
    }
    return render(request, 'main_app/contact.html',context)

def properties(request):
    p = Profile.objects.all()
    pp = Profile_p.objects.all()
    p_2 = Profile_2.objects.all()
    p_3 = Profile_3.objects.all()
    p_4 = Profile_4.objects.all()
    p_5 = Profile_5.objects.all()
    p_6 = Profile_6.objects.all()
    p_7 = Profile_7.objects.all()
    p_8 = Profile_8.objects.all()

    context = {
        'p':p,
        'pp':pp,
        'p_2':p_2,
        'p_3':p_3,
        'p_4':p_4,
        'p_5':p_5,
        'p_6':p_6,
        'p_7':p_7,
        'p_8':p_8,

        
    }
    return render(request, 'main_app/properties.html',context)

def property_single(request):
    return render(request, 'main_app/property-single.html')

def services(request):
    return render(request, 'main_app/services.html')
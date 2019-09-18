from django.shortcuts import render
from django.http import HttpResponse
from . forms import contactForm
from .models import contact,experience
from .import quote
import random
# Create your views here.


def home(request):
    quotes = quote.quote()
    rand = random.randrange(0,4,1)
    print(quotes[rand])
    rand_quote = quotes[rand]
    return render(request,'main/head.html',{'quote':rand_quote, "experience": experience.objects.all})

def projects(request):
    return render(request, 'main/projects.html')

def contactMe(request):
    context = {}
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            newContact = contact()
            newContact.name = form.cleaned_data['name']
            newContact.email = form.cleaned_data['email']
            newContact.phone = form.cleaned_data['phone']
            newContact.message = form.cleaned_data['message']
            newContact.save()
            success = 'Great! I\'ll get back to you very soon!'
            context.update({'success': success})
    form = contactForm()
    context.update({'form':form})
    return render(request, 'main/contact me.html', context)
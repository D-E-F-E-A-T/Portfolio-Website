from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import contactForm, experienceForm, projectForm
from .models import contact,experience, project
from django.contrib import messages
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

    return render(request, 'main/projects.html',{"projects": project.objects.all})

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


def newExp(request):
    context = {}
    if request.method == 'POST':
        form = experienceForm(request.POST)
        if form.is_valid():
            exp = experience()
            exp.title = form.cleaned_data['title']
            exp.date = form.cleaned_data['date']
            exp.content = form.cleaned_data['content']
            exp.save()
            success = 'Form saved!'
            context.update({'success': success})
    form = experienceForm()
    context.update({'form': form})
    return render(request,"main/newexp.html", context)

def newProj(request):
    context = {}
    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid():
            proj = project()
            proj.title = form.cleaned_data['title']
            proj.description = form.cleaned_data['description']
            proj.link = form.cleaned_data['link']
            proj.code_link = form.cleaned_data['code_link']
            proj.save()
            success = 'Form saved!'
            context.update({'success': success})
    form = projectForm()
    context.update({'form': form})
    return render(request,"main/newproj.html", context)
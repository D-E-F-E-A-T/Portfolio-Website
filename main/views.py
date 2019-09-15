from django.shortcuts import render
from django.http import HttpResponse
from . forms import contactForm

import praw
import random
# Create your views here.

def quote():
    reddit = praw.Reddit(client_id = 'AW7uCde_gwkGeg',
                     client_secret = 'ymlEQKiKR339IPal-cM6nk4nyZQ',
                     username = 'prawAndDjango',
                     password = 'QQbdTJHPHT22',
                     user_agent = 'praw')

    subreddit = reddit.subreddit('quotes')

    hot_python = subreddit.hot(limit = 7)

    submission_list = []

    for submission in hot_python:
            if not submission.stickied:
                submission_list.append(submission.title)

    return submission_list

def home(request):
    quotes = quote()
    rand = random.randrange(0,4,1)
    print(quotes[rand])
    rand_quote = quotes[rand]
    return render(request,'main/head.html',{'quote':rand_quote})

def projects(request):
    return render(request, 'main/projects.html')

def contactMe(request):
    form = contactForm()
    return render(request, 'main/contact me.html', {'form': form})
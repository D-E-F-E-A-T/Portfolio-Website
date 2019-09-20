from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('projects', views.projects, name = 'projects'),
    path('contact-me', views.contactMe, name = 'contact'),
    path('newexp', views.newExp, name="newexp"),
    path('newproj', views.newProj, name="newproj"),
]

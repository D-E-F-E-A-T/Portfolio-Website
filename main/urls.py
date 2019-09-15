from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('projects', views.projects, name = 'projects'),
    path('contact-me', views.contactMe, name = 'contact')
]

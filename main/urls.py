from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('projects', views.projects, name = 'projects'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('showDoc/', views.showDoc, name='showDoc'),
    path('showPat/', views.showPat, name='showPat'),

]
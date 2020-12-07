from django.urls import path
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.Form.getForm, name='form'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.form_upload, name='form-upload'),
    path('', views.documents, name='documents'),
    path('<str:pk>/', views.show, name='show'),


]

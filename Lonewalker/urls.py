from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_poster_id>/', views.movie_detail, name='movie_detail'),
    path('merch', views.merch, name='merch'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact_submit/', views.contact_submit, name='contact_submit'),
]
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request,HttpResponseRedirect
from django.urls import reverse

from .models import MoviePoster, MovieContent, MerchPoster,Actor, Team, Company


# Create your views here.
def index(request):
    movies = MoviePoster.objects.all()
    for movie in movies:
        movie.detail_url = reverse('movie_detail', args=[movie.id])
    return render(request, "Lonewalker/home.html", {"movies": movies})


def movie_detail(request, movie_poster_id):
    movie_poster = get_object_or_404(MoviePoster, id=movie_poster_id)
    movie_content = MovieContent.objects.filter(movie_poster=movie_poster).first()

    actors = movie_content.cast.all() if movie_content else []

    context = {
        'movie_poster': movie_poster,
        'movie_content': movie_content,
        'cast': actors
    }

    return render(request, 'Lonewalker/movie_details.html', context)


def merch(response):
    merchandise = MerchPoster.objects.all()
    return render(response, "Lonewalker/merch.html", {"merchandise":merchandise})

def about(response):
    about_us = Team.objects.all()
    company_profiles = Company.objects.all()
    context = {
        "about_us":about_us,
        "company_profiles": company_profiles,
    }

    return render(response, "Lonewalker/about.html", context)


def contact(request):
    return render(request, 'Lonewalker/contact.html')
def contact_submit(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        return HttpResponseRedirect(reverse('contact_success'))

    return render(request, 'Lonewalker/contact.html')

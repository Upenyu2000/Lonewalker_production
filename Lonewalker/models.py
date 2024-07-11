from django.db import models
from embed_video.fields import EmbedVideoField


class Actor(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class MoviePoster(models.Model):
    poster_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=300)
    cast = models.ManyToManyField(Actor, blank=True, related_name='movie_posters')

    def __str__(self):
        return f"{self.title} - Poster: {self.poster_image.url if self.poster_image else 'No poster'}"


class MerchPoster(models.Model):
    merch_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=300)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - Poster: {self.merch_image.url if self.merch_image else 'No poster'}"


class MovieContent(models.Model):
    VIDEO_TYPES = [
        ('youtube', 'YouTube'),
        ('vimeo', 'Vimeo'),
        ('direct', 'Direct Video URL'),
    ]
    video = EmbedVideoField(null=True, blank=True)
    video_type = models.CharField(max_length=10, choices=VIDEO_TYPES, default='youtube')
    movie_poster = models.ForeignKey(MoviePoster, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    cast = models.ManyToManyField(Actor, blank=True, related_name='movie_contents')

    def __str__(self):
        return f"{self.description}"


class Team(models.Model):
    full_name = models.CharField(max_length=300, blank=True, null=True)
    role = models.CharField(max_length=600, blank=True, null=True)
    employee_details = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} {self.role} {self.employee_details}"


class Company(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    company_profile = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.company_profile}"

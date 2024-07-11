from django.contrib import admin
from .models import MoviePoster, MovieContent, MerchPoster, Actor, Team, Company
from embed_video.admin import AdminVideoMixin


class MovieContentInline(AdminVideoMixin, admin.StackedInline):
    model = MovieContent
    extra = 1


class ActorInline(admin.TabularInline):
    model = MoviePoster.cast.through
    extra = 1


@admin.register(MoviePoster)
class MoviePosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'has_poster')
    inlines = [MovieContentInline, ActorInline]

    def has_poster(self, obj):
        return bool(obj.poster_image)

    has_poster.boolean = True


@admin.register(MovieContent)
class MovieContentAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('movie_poster', 'description', 'video_type')
    fields = ('movie_poster', 'description', 'video_type', 'video', 'cast')
    filter_horizontal = ('cast',)


@admin.register(MerchPoster)
class MerchPosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'merch_image', 'price')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Team)
class TeamManagement(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'employee_details', 'image')


@admin.register(Company)
class CompanyDetails(admin.ModelAdmin):
    list_display = ('title', 'company_profile')

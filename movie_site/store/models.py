from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )


class Profile(AbstractUser):
    age = models.SmallIntegerField(validators=[MinValueValidator(18),
                                               MaxValueValidator(60)],
                                   null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.username}'


class Country(models.Model):
    country_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    director_image = models.ImageField(upload_to='director_images')

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    actor_image = models.ImageField(upload_to='actor_images')

    def __str__(self):
        return self.actor_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=32)
    year = models.DateField()
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    TYPE_CHOICES = (
        ('144p', '144p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    )
    types = MultiSelectField(max_length=16, choices=TYPE_CHOICES, max_choices=50)
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movie_trailer')
    movie_image = models.ImageField(upload_to='movie_images')
    status_movie = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return self.movie_name

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class MovieLanguages(models.Model):
    language = models.CharField(max_length=16)
    video = models.FileField(upload_to='movie_languages')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_language')

    def __str__(self):
        return f'{self.language} - {self.movie}'


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='movie_moments')


class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.CharField(max_length=16, choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class Favorite(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateField(auto_now_add=True)


#
# DRF:
# .env,
# language(en, ru, +1)
# filter(country, year от и до, janre, status_movie, actor, director),
# search(movie_name),
# ordering(year),
# swagger,
# permission,
# jwt (login),
# req.txt,
# github,
# aws > ТГ
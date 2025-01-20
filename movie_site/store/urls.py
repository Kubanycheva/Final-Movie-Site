from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'movie', MovieListViewSet, basename='movie-list')
router.register(r'movie-detail', MovieDetailViewSet, basename='movie-detail')

router.register(r'users', ProfileViewSet, basename='users-list')

router.register(r'country', ProfileViewSet, basename='country-list')
router.register(r'user-detail', ProfileViewSet, basename='country-detail')

router.register(r'director', DirectorListViewSet, basename='director-list')
router.register(r'director-detail', DirectorDetailViewSet, basename='director-detail')

router.register(r'actor', ActorListViewSet, basename='actor-list')
router.register(r'actor-detail', ActorDetailViewSet, basename='actor-detail')

router.register(r'genre', GenreViewSet, basename='genre-list')
router.register(r'genre-detail', GenreViewSet, basename='genre-detail')

router.register(r'languages', MovieLanguagesViewSet, basename='languages-list')
router.register(r'languages-detail', MovieLanguagesViewSet, basename='languages-detail')

router.register(r'moments', MomentsViewSet, basename='moments-list')
router.register(r'moments-detail', MomentsViewSet, basename='moments-detail')

router.register(r'rating', RatingViewSet, basename='rating-list')
router.register(r'rating-detail', RatingViewSet, basename='rating-detail')

router.register(r'favorite', FavoriteViewSet, basename='favorite-list')
router.register(r'favorite-detail', FavoriteViewSet, basename='favorite-detail')

router.register(r'favorite_movie', FavoriteMovieViewSet, basename='favorite_movie-list')
router.register(r'favorite_movie-detail', FavoriteMovieViewSet, basename='favorite_movie-detail')

router.register(r'history', HistoryViewSet, basename='history-list')
router.register(r'history-detail', HistoryViewSet, basename='history-detail')


urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

# path('', MovieListViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
# path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                               'delete': 'destroy'}), name='movie_detail'),
#
# path('users/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile_list'),
# path('users/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',

#
# path('country/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country_list'),
# path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                   'delete': 'destroy'}), name='country_detail'),
#
#
# path('director/', DirectorListViewSet.as_view({'get': 'list', 'post': 'create'}), name='director_list'),
# path('director/<int:pk>/', DirectorDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                     'delete': 'destroy'}), name='director_detail'),
#
#
# path('actor/', ActorListViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
# path('actor/<int:pk>/', ActorDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                               'delete': 'destroy'}), name='actor_detail'),
#
#
# path('genre/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='genre_list'),
# path('genre/<int:pk>/', GenreViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                               'delete': 'destroy'}), name='genre_detail'),
#
#
# path('languages/', MovieLanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='languages_list'),
# path('languages/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                            'delete': 'destroy'}), name='languages_detail'),
#
#
# path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='moments_list'),
# path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                   'delete': 'destroy'}), name='moments_detail'),
#
#
# path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
# path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                 'delete': 'destroy'}), name='rating_detail'),
#
#
# path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_list'),
# path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                     'delete': 'destroy'}), name='favorite_detail'),
#
#
# path('favorite_movie/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_list'),
# path('favorite_movie/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                                'delete': 'destroy'}), name='favorite_detail'),
#
#
# path('history/', HistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='history_list'),
# path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                   'delete': 'destroy'}), name='history_detail'),




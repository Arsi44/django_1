from django.apps import AppConfig
from django.urls import path
from . import views

class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'

urlpatterns = [
    path("", views.MoviesView.as_view()),
    # path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    # path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"  # есть значение по умолчанию, но лучше указывать явно!

    # View
    # def get(self, request):
    #     movies = Movie.objects.all()
    #     return render(request, "movies/movies.html", {'movie_list': movies})


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"  # по какому атрибуту искать запись (по url)
    template_name = "movies/movie_detail.html"    # есть значение по умолчанию, но лучше указывать явно!



# class AddReview(View):
#     """Отзывы"""
#     def post(self, request, pk):
#         form = ReviewForm(request.POST)
#         movie = Movie.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.movie = movie
#             form.save()
#         return redirect(movie.get_absolute_url())

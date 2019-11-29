from django.urls import path, include
from movie_api import views

urlpatterns = [
    path('movie/', views.MovieList.as_view()),
    path('movie/<int:pk>/', views.MovieDetail.as_view())

]

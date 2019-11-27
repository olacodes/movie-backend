from django.shortcuts import render

from .models import Movie
from .serializers import MovieSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class MovieList(APIView):
    '''
    List all movie, or create a new movie
    '''
    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        movie = MovieSerializer(data=request.data)
    
        if movie.is_valid():
            movie.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)
        return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetail(APIView):
    """
    Retrieve, update or delete a movie instance
    """

    def get_movie(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_movie(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from django.shortcuts import render

from .models import Movie
from .serializers import MovieSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MovieList(APIView):
    '''
    This MoiveList API method List all movies that are available and 
    return a serialized data in json format and an appropriate HTTP response code
    
    It can also create movie by passing in data, deserialised the data, 
    check if data is_valid and save it in the database
    '''
    serializer_class = MovieSerializer
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
    This method helps to Update, Retrieve and Delete a movie instance and 
    return an appropriate Http response
    
    """
    serializer_class = MovieSerializer
    def get_movie(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
    """
    This method helps to get a particular movie by using 
    the movie id and return a serialised json object
    """
    def get(self, request, pk):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    """
    This method helps to Update a movie and return a serialized json data and HTTP response
    """
    def put(self, request, pk):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    This delete a movie and return the status code of 
    status.HTTP_204_NO_CONTENT
    """
    def delete(self, request, pk):
        movie = self.get_movie(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


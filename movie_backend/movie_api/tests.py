from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Movie
import json
from django.urls import reverse
# from rest_framework.test import APIRequestFactory
# Create your tests here.


class MovieTest(APITestCase):

    def test_post(self):
        data = {
            "genre": "drama",
            "title": "last blood",
            "link" : "https://www.youtube.com/watch?v=4vWg5yJuWfs",
            "image": "https://en.wikipedia.org/wiki/Rambo:_Last_Blood#/media/File:Rambo_-_Last_Blood_official_theatrical_poster.jpg",
            "detail": "syvester stallon movie"
        }
        client = APIClient()
        url = '/movies/movie/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GetMovie(APITestCase):
    url = '/movies/movie/1/'

    def setUp(self):
        self.data = Movie.objects.create(
            id = 1,
            genre = "drama",
            title = "last blood",
            link = "https://www.youtube.com/watch?v=4vWg5yJuWfs",
            image = "https://en.wikipedia.org/wiki/Rambo:_Last_Blood#/media/File:Rambo_-_Last_Blood_official_theatrical_poster.jpg",
            detail = "syvester stallon movie"
        )
    def test_get(self):
        print(self.url)
        # url = '/movies/movie/'
        response = self.client.get(self.url)
        print(response)
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_one_movie(self):
        response = self.client.get(self.url)
        # print(Movie.objects.get(id=1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_movie(self):
        
        data = {
            "pk":1,
            "genre":"action",
            "title" :"last blood",
            "link" : "https://www.youtube.com/watch?v=4vWg5yJuWfs",
            "image" : "https://en.wikipedia.org/wiki/Rambo:_Last_Blood#/media/File:Rambo_-_Last_Blood_official_theatrical_poster.jpg",
            "detail" : "syvester stallon movie"
        }
        url_one ='/movies/movie/1/' 
        response = self.client.put(url_one, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['genre'], 'action')

    def test_delete_movie(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

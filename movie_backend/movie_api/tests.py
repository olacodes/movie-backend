from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Movie
import json
from django.urls import reverse
from mockData.data import MockData

class MovieTest(APITestCase):
    """
    This method test the post resquest method and assert that the 
    HTTP response status is HTTP_201_CREATED 
    """
    def test_post(self):
        client = APIClient()
        url = '/movies/movie/'
        response = self.client.post(url, MockData.data_post(), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GetMovie(APITestCase):
    url = '/movies/movie/1/'
    def setUp(self):
        self.data = Movie.objects.create(**MockData.set_up())
    
    """
    This method test the get resquest method and assert that the 
    HTTP response status is HTTP_200_OK 
    """
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    This method test the get a movie resquest method and assert that the 
    HTTP response status is HTTP_200_OK 
    """

    def test_get_one_movie(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    This method test the UPDATE resquest method and assert that the 
    HTTP response status is HTTP_200_OK and  also check the response data for change
    """
    def test_update_movie(self):

        response = self.client.put(self.url, MockData.data_update())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['genre'], 'action')

    """
    This method test the DELETE resquest method and assert that the 
    HTTP response status is HTTP_204_NO_CONTENT
    """

    def test_delete_movie(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

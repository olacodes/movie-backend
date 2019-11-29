from rest_framework import serializers
from .models import Movie

"""
The serializer class seriliaze and deserialize the data
"""
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

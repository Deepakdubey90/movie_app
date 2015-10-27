from rest_framework import serializers
from .models import (
        Movie,
        Category
)
from django.contrib.auth import get_user_model
User = get_user_model()


class MovieGetSerializer(serializers.ModelSerializer):
    """To serialize Movie for GET. """

    id = serializers.ReadOnlyField()
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return [g.movie_type for g in obj.category.all()] if obj.category else []

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'featured_image', 'movie_length', 'movie_release_date', 'category')


class MoviePostSerializer(serializers.ModelSerializer):
    """To serialize Movie for POST. """

    id = serializers.ReadOnlyField()
    class Meta:
        model = Movie
        field = ('id', 'title', 'description', 'featured_image', 'movie_length', 'movie_release_date', 'category',)
        exclude = ('deleted_on', 'user',)


class CategorySerializer(serializers.ModelSerializer):
    """To serialize category. """

    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('id', 'movie_type', 'value')

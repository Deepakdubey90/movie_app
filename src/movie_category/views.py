import django_filters
from rest_framework import viewsets
from utils import permissions
from rest_framework.response import Response
from rest_framework import filters
from .models import (
    Movie,
    Category
)
from .serializers import (
    MovieGetSerializer,
    MoviePostSerializer,
    CategorySerializer
)


class MovieFilter(django_filters.FilterSet):
    movie_length = django_filters.NumberFilter( lookup_type='lte')
    movie_release_date = django_filters.NumberFilter(lookup_type='lte')
    
    class Meta:
        model = Movie
        order_by = ['movie_length', 'movie_release_date']
        fields = ['id', 'title', 'description', 'featured_image', 'movie_length', 'movie_release_date', 'category']
    
    
class MovieViewSet(viewsets.ModelViewSet):
    """
    List of all movie.
    """
    permission_classes = (permissions.ReadAllWriteOnlyAdminPermission, )
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer_class = MovieGetSerializer
        else:
            serializer_class = MoviePostSerializer
            
        return serializer_class


    def get_queryset(self):
        movies = Movie.objects.filter(deleted_on__isnull=True)
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            movies = Movie.objects.filter(user_id=self.request.user.id)
        return movies
            
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MovieFilter
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    """
    List of all category of movie.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

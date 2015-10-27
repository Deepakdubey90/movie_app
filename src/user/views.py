from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import (list_route, detail_route)
from rest_framework import status, views
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, UserDetailSerializer
from user.models import User
from utils import permissions


class UserDetailViewSet(viewsets.ModelViewSet):
    """
    user viewset
    """
    permission_classes = (permissions.ReadAllWriteOnlyAdminPermission, )
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class AuthUserViewSet(APIView):
    """
    AuthUserViewSet
    """
    permission_classes = (permissions.ReadAllWriteOnlyAdminPermission, )
    serializer_class = UserSerializer

    @detail_route(methods=['delete'], url_path='id')
    def delete(self, request):
        """
	this model delete will log the user out
	"""
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def post(self, request):
        """
	this model will log the authenticated user in
	"""
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(username=username, password=password)
        if account is not None:
            if account.is_active:
                login(request, account)
                return Response(None)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
            
class MeViewSet(APIView):
    """
    this model will show thw details of user logged in "
    """
    serializer_class = UserSerializer
    def get(self, request):
        """
	this method will return logged in user details
	"""
        user = request.user
        if user.is_authenticated():
            serializer = UserSerializer(user)
            return Response(serializer.data)
            return Response({
                'status': 'User not found',
                'message': 'Please log in first'
            }, status=status.HTTP_204_NO_CONTENT)
            

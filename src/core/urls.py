from django.conf.urls import include, url
from django.contrib import admin
from .views import IndexView, ApiView
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from rest_framework.routers import DefaultRouter
from movie_category.views import (MovieViewSet, CategoryViewSet)
from user.views import (UserDetailViewSet,AuthUserViewSet,MeViewSet)


router = DefaultRouter()
router.register(r'movie', MovieViewSet, base_name="movie")
router.register(r'category', CategoryViewSet, base_name="category")
router.register(r'user',  UserDetailViewSet, base_name="user")

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/auth', AuthUserViewSet.as_view()),
    url(r'^user/me', MeViewSet.as_view()),
    url(r'^$', IndexView.as_view()),
    url(r'^api', ApiView.as_view()),
    url(r'^', include(router.urls)),
    url(r'authentication/', include('rest_framework.urls',
				    namespace='rest_framework')),
] + router.urls

if not settings.DEBUG:
    urlpatterns += [
	url(r'^static/(?P<path>.*)$', serve,
	    {'document_root': settings.STATIC_ROOT})
    ]

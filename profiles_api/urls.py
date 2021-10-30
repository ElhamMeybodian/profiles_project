import rest_framework.authentication
from django.urls import path, include, re_path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    # path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

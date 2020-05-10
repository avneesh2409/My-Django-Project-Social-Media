from django.urls import re_path,path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'heroes', HeroViewSet)
router.register(r'student',StudentViewSet)

app_url = 'https://localhost:8000/socialmedia'
urlpatterns = [
    re_path(r'^$', index, name='index'),
    path('home/', HomePageView.as_view(), name='home'),
    re_path(r'^helloworld/$',HelloWorldView.as_view(),name="helloworld"),
    path('api/', include(router.urls)),
    path('herolist/',HeroList.as_view(),name="herolist"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
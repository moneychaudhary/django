from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    url(r'^test', views.HelloAPIView.as_view()),
    url(r'^''', include(router.urls)),

]
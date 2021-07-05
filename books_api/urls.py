from django.urls import path,include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()

# registering the book with router
router.register('',BookViewSet,basename='book')

urlpatterns = [
    path('',include(router.urls)),
]
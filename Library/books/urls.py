from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books import views

router = DefaultRouter()
router.register('books', views.BookViewSet,  basename='books')


urlpatterns = [
  path('', include(router.urls)),
  path('auth/', include('rest_framework.urls')),
]


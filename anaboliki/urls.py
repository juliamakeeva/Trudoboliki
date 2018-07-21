from django.urls import path
from .views import catalog, city


urlpatterns = [
    path('', catalog),
    path('<int:town>/', city, name='city')
]
from django.urls import path
from .views import catalog, city
from .views import new_town, edit_town

urlpatterns = [
    path('', catalog),
    path('<int:town>/', city, name='city'),
    path('new/', new_town),
    path('edit/<int:town>/', edit_town),
]
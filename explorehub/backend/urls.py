from django.urls import path
from .views import AccommodationListCreate, ActivityListCreate, CarListCreate, PromoListCreate, ProfileListCreate

urlpatterns = [
    path('accommodations/', AccommodationListCreate.as_view(), name='accommodations'),
    path('activities/', ActivityListCreate.as_view(), name='activities'),
    path('cars/', CarListCreate.as_view(), name='cars'),
    path('promos/', PromoListCreate.as_view(), name='promos'),
    path('profiles/', ProfileListCreate.as_view(), name='profiles'),
]

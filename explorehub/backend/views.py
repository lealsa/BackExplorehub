from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Accommodation, Activity, Car, Promo, Profile
from .serializers import AccommodationSerializer, ActivitySerializer, CarSerializer, PromoSerializer, ProfileSerializer
from .filters import AccommodationFilter, ActivityFilter, CarFilter, PromoFilter, ProfileFilter

class AccommodationListCreate(generics.ListCreateAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AccommodationFilter

class ActivityListCreate(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ActivityFilter

class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter

class PromoListCreate(generics.ListCreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PromoFilter

class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfileFilter

import django_filters
from .models import Accommodation, Activity, Car, Promo, Profile

class AccommodationFilter(django_filters.FilterSet):
    class Meta:
        model = Accommodation
        fields = ['type', 'city', 'stars']

class ActivityFilter(django_filters.FilterSet):
    labels = django_filters.CharFilter(method='filter_labels')

    class Meta:
        model = Activity
        fields = ['type']

    def filter_labels(self, queryset, name, value):
        return queryset.filter(labels__contains=[value])
class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['type', 'fuelType', 'transmission', 'passengers']

class PromoFilter(django_filters.FilterSet):
    class Meta:
        model = Promo
        fields = ['type']

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'location']

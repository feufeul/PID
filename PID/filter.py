import django_filters
from PID.models import Show


class ShowFilter(django_filters.FilterSet):
    class Meta:
        model = Show
        fields = ['price', 'title']

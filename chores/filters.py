import django_filters
from chores.models import ChoresPost


class ChoresPostFilters(django_filters.FilterSet):
    class Meta:
        model = ChoresPost
        fields = {
            'name': ['exact'],
            'category': ['exact'],
            'date_of_post': ['exact'],
            'budget': ['lt', 'gt'],
            'date': ['exact'],
        }

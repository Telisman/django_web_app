import django_filters
from clients.models import ClientsUsers


class FilterUser(django_filters.FilterSet):
    class Meta:
        model = ClientsUsers
        fields = {
            'user_type': ['exact'],
            'last_name': ['exact'],
            'first_name': ['exact'],
            'username': ['exact'],
        }

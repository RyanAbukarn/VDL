import django_filters
from .models import Parser


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Parser
        fields = '__all__'

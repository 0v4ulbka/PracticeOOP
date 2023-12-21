from django_filters import FilterSet
from .models import Application


class ApplicationFilter(FilterSet):
    class Meta:
        model = Application
        fields = ('status',)

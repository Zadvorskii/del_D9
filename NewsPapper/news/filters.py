from django_filters import FilterSet, CharFilter, DateTimeFromToRangeFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import *


# создаём фильтр
class PostFilter(FilterSet):
    datetime = DateTimeFromToRangeFilter()
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {
            'heading': ['icontains'],
            'text': ['icontains'],
            'category__name': ['icontains'],

        }
from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post
from django.forms import DateInput
import django_filters
from django import forms


# создаём фильтр
class NewsFilter(FilterSet):

    author = django_filters.CharFilter(
        field_name='author',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
    )

    Post_time = django_filters.DateFilter(
        field_name='Post_time',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        lookup_expr='gt',
    )
    Post_title = django_filters.CharFilter(
        field_name='Post_title',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
    )
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = ['Post_title', 'author', 'Post_time']  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)



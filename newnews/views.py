from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from datetime import datetime
from .models import Post, Category, PostCategory, Author
from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .filters import NewsFilter
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-Post_time']
    paginate_by = 1




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['categories'] = PostCategory.objects.all()
        context['form'] = NewsForm()
        context['is_authors'] = self.request.user.groups.filter(name='authors').exists()
        return context



class NewsDetailView(DetailView):
    model = Post
    template_name = 'newnews/news_detail.html'
    context_object_name = 'news_detail'
    queryset = Post.objects.all()


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'newnews/news_create.html'
    form_class = NewsForm
    success_url = '/news/'
    permission_required = ('news.add_post', 'news.view_post')





# дженерик для редактирования объекта
class NewsUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    template_name = 'newnews/news_create.html'
    success_url = '/news/'
    form_class = NewsForm
    permission_required = ('news.change_post', 'news.view_post')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class NewsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'newnews/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = ('news.delete_post', 'news.view_post')




class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-Post_time')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['categories'] = PostCategory.objects.all()
        context['form'] = NewsForm()
        return context



import random

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from blog.models import Article


class Add_blog(View):
    def get(self,request):
        return render(request,'blog/post_article.html')

    def post(self,request):
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

        data = {

            'title':title,
            'content':content,
        }
        return render(request,'blog/article_detail.html',context=data)


class Index(ListView):
    template_name = 'blog/blog_index.html'
    paginate_by = 10
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.all()

    def get_queryset_data(self, *, object_list=None, **kwargs):
        article_list = Article.objects.get_queryset()
        return article_list



class Article_detail(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_obj_name = 'article_detail'
    pk_url_kwarg = 'article_id'
    #
    # def get_object(self, queryset=None):
    #
    #
    # def get_context_data(self, **kwargs):
    #
    #     return super().get_context_data()


def randomnum():

    nums = Article.objects.count()
    random_num = random.randrange(nums)
    data = {
        'random_num':random_num
    }
    return JsonResponse(data)



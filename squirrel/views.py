from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from squirrel.models import SquirrelItem


class SquirrelIndex(ListView):
    template_name = 'squirrel/squirrel_index.html'
    paginate_by = 10
    context_object_name = 'squirrel_list'

    def get_queryset(self):
        return SquirrelItem.objects.all()

    def get_queryset_data(self,*, object_list=None, **kwargs):
        squirrel_list = SquirrelItem.objects.get_queryset()

class Squirrel_Article_detail(DetailView):
    model = SquirrelItem
    template_name = 'squirrel/squirrel_article_detail.html'
    context_obj_name = 'squirrel_detail'
    pk_url_kwarg = 'article_id'

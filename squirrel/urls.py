from django.urls import re_path

from squirrel import views

urlpatterns = [

    re_path(r'^squirrelindex/$', views.SquirrelIndex.as_view(), name='squirrel_index'),
    re_path(r'^squirrelindex/(?P<page>\d+)/', views.SquirrelIndex.as_view(), name='squirrel_index_page'),
    re_path(r'^squirrelarticledetail/(?P<article_id>\d+)/', views.Squirrel_Article_detail.as_view(), name='squirrel_article_detail'),

]
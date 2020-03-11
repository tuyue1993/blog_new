from django.urls import re_path

from blog import views

urlpatterns = [
    re_path(r'^addblog/$',views.Add_blog.as_view(),name='blog'),
    re_path(r'^blogindex/$',views.Index.as_view(),name='index'),
    re_path(r'^blogindex/(?P<page>\d+)/',views.Index.as_view(),name='index_page'),
    re_path(r'^articledetail/(?P<article_id>\d+)/',views.Article_detail.as_view(),name='article_detail'),
    re_path(r'^random/',views.randomnum,name='random'),

]
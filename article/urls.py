from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                        #url(r'^admin/', include(admin.site.urls)),
                        #если в адресе есть "basic" то нас перенаправляет пр этому адресу 'article.views.basic_one' во views
    #url(r'^1/', 'article.views.basic_one'),
    url(r'^1', 'article.views.basic_one'),
    url(r'^2', 'article.views.template_two'),
    url(r'^3', 'article.views.template_three_simple'),
    url(r'^articles/all$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)$', 'article.views.article'),             # (?P<article_id>\d+) - переменная которую мы передaдим в качестве параметров функции
    url(r'^articles/addlike/(?P<article_id>\d+)$', 'article.views.addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)$', 'article.views.addcomment'),
    url(r'page/(\d+)$', 'article.views.articles'),
    url(r'^', 'article.views.articles'),
)
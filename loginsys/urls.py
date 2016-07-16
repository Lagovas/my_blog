from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                        #url(r'^admin/', include(admin.site.urls)),
                        #если в адресе есть "basic" то нас перенаправляет пр этому адресу 'article.views.basic_one' во views

    url(r'^login/$', 'loginsys.views.login'),
    url(r'^logout/$', 'loginsys.views.logout'),
    url(r'^register/$', 'loginsys.views.register'),
)
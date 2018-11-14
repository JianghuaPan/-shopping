from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [  
    url(r'^$',views.index,name='index'),
    url(r'^reindex',views.reindex,name='myweb_reindex'),
    url(r'^urlpath',views.urlpath,name='myweb_urlpath'),

]
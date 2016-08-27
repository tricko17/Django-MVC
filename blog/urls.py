from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='blog_index'),
    url(r'^post/add/$', views.post_add, name='post_add'),
    # url(r'^detail/$', views.coeg, name='blog_coeg'),
    url(r'^details/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^details/edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'^details/delete/(?P<pk>[0-9]+)/$', views.post_delete, name='post_delete'),
]

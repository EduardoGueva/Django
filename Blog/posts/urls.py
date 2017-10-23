from django.conf.urls import url

from . import views

urlpatterns=[
url(r'^$',views.index,name='post_index'),
url(r'^add.html$',views.add),
url(r'^update.html$',views.update,name='posts_update'),
#url(r'^delete/$',views.delete,name='posts_delete'),
]
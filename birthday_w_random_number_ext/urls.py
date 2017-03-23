from django.conf.urls import url

from . import views

app_name = 'br_users'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'add/$', views.AddView.as_view(), name='add_user'),
    url(r'csv/$', views.csv_view, name='csv_data'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EditView.as_view(), name='edit_user'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete_user'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='user_info'),
]

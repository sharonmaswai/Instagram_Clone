from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    
    url('^$',views.index,name='index'),
    url(r'^new/profile$', views.create_profile, name='create-profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^home/$', views.home, name='home')
]
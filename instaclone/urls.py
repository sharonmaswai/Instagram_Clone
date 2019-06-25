from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    
    url('^$',views.index,name='index'),
    url(r'^new/profile$', views.create_profile, name='create-profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^home/$', views.home, name='home'),
    url(r'^comment/(\d+)$', views.comment, name='comment'),
         url(r'^comment/(\d+)$', views.comment, name='comment'),
    url(r'^new/post/$', views.new_post, name='new-post')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
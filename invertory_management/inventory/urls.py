from django.conf.urls import url
from .views import *

urlpatterns=[

    url(r'^$',index, name='index'),
    url(r'^display_laptop$', display_laptops, name='display_laptops'),
    url(r'^display_desktop$', display_desktops, name='display_desktops'),
    url(r'^display_mobile$', display_mobile, name='display_mobile'),
    url(r'^add_Laptop$',add_Laptop,name='add_laptop'),
    url(r'^add_Desktop$',add_Desktop,name='add_desktop'),
    url(r'^add_Mobile$',add_Mobile,name='add_mobile'),
    url(r'^edit_laptop/(?P<pk>\d+)$',edit_laptop,name='edit_laptop'),
    url(r'^edit_desktop/(?P<pk>\d+)$',edit_desktop,name='edit_desktop'),
    url(r'^edit_mobile/(?P<pk>\d+)$',edit_mobile,name='edit_mobile'),
    url(r'^delete_desktop/(?P<pk>\d+)$',delete_desktop,name='delete_desktop'),
    url(r'^delete_laptop/(?P<pk>\d+)$',delete_laptop,name='delete_laptop'),
    url(r'^delete_mobile(?P<pk>\d+)$',delete_mobile,name='delete_mobile'),


]



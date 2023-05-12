from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


urlpatterns=[
    path('index1',views.index1,name='index1'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
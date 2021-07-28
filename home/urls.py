from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path("song/<slug>",views.post, name="posts"),
    path("tag/<slug>",views.label, name="label"),
    path("download",views.download, name="download"),
    path("search",views.search,name='search'),
    path("singer/<singer>",views.singer,name='singer'),
    path("ss",views.ggg,name='ggg'),
    path("all/<categery>",views.seeall,name='seeall'),
]

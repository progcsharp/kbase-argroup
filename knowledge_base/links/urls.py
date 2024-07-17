from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path('article/<int:article_id>/', views.article, name="article"),
    path('dawnload/<int:article_id>/', views.article, name='download')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categories/<str>:category', views.PostCategory.as_view(), name='categories'),
    path('search/', views.PostSearch.as_view(), name='search'),
    path('post/<int:id>', views.PostDetails.as_view(), name='post'),
]

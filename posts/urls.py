from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categories/<category>:category', views.PostCategory.as_view(), name='categories'),
    path('search/', views.PostSearch.as_view(), name='search'),
    path('post/<slug:pk>', views.PostDetails.as_view(), name='post'),
]

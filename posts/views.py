from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When

class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(published=True)
        qs = qs.annotate(numcomments=Count(Case(When(comment__published=True, then=1))))
        return qs

class PostSearch(PostIndex):
    template_name = 'posts/search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        searched = self.request.GET.get('text')
        if not searched:
            return qs
        qs = qs.filter(Q(title__icontains=searched) | Q(content__icontains=searched))
        # qs = qs.annotate(numcomments=Count(Case(When(comment__published=True, then=1))))
        return qs

class PostCategory(PostIndex):
    template_name = 'posts/categories.html'

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.kwargs.get('category', None)
        if not category:
            return qs
        qs = qs.filter(catpost__catname__iexact=category)
        return qs

class PostDetails(UpdateView):
    pass

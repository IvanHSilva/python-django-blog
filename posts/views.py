from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views import View
from django.db.models import Q, Count, Case, When
from django.db import connection
from django.contrib import messages
from .models import Post
from comments.models import Comment
from comments.forms import FormComment


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('catpost')
        qs = qs.order_by('-id').filter(published=True)
        qs = qs.annotate(numcomments=Count(Case(When(comment__published=True, then=1))))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['connection'] = connection
        return context

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

class PostDetails(View):
    template_name = 'posts/details.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, published=True)
        self.context = {
            'post': post,
            'comments': Comment.objects.filter(published=True, post=post.id),
            'form': FormComment(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.context['form']

        if not form.is_valid():
            return render(request, self.template_name, self.context)

        comment = form.save(commit=False)

        if request.user.is_authenticated:
            comment.user = self.request.user
        comment.post = self.context['post']
        comment.save()
        messages.success(self.request, 'Comentário enviado com sucesso. Aguarde aprovação.')

        return redirect('post', pk=self.kwargs.get('pk'))


# class PostDetails(UpdateView):
#     template_name = 'posts/details.html'
#     model = Post
#     form_class = FormComment
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.get_object()
#         comments = Comment.objects.filter(published=True, post=post.id)
#         context['comments'] = comments
#
#         return context
#
#     def form_valid(self, form):
#         post = self.get_object()
#         comment = Comment(**form.cleaned_data)
#         comment.post = post
#
#         if self.request.user.is_authenticated:
#             comment.user = self.request.user
#         comment.save()
#         messages.success(self.request, 'Comentário enviado com sucesso. Aguarde aprovação.')
#
#         return redirect('post', pk=post.id)

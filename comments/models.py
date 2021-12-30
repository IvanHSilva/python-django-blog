from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-Mail')
    comment = models.TextField(verbose_name='Comentário')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    comdate = models.DateTimeField(default=timezone.now, verbose_name='Data')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.name

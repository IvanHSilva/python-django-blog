from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    postdate = models.DateTimeField(default=timezone.now, verbose_name='Data Post')
    content = models.TextField(verbose_name='Conteúdo')
    excert = models.TextField(verbose_name='Excerto')
    catpost = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    image = models.ImageField(upload_to='postimg/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.title

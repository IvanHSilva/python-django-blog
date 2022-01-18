from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from PIL import Image

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.imgsresize(self.image.name, 800)

    @staticmethod
    def imgsresize(img, newwidth):
        imgpath = settings.MEDIA_ROOT / img
        img = Image.open(imgpath)
        width, height = img.size
        # print(f'Tamanho original: {width} X {height}')
        newheight = round((newwidth * height) / width)
        # print(f'Novo tamanho: {newwidth} X {newheight}')

        if width > newwidth:
            newimg = img.resize((newwidth, newheight), Image.ANTIALIAS)
            newimg.save(imgpath, optimize=True, quality=75)
            newimg.close()

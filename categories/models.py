from django.db import models

class Category(models.Model):
    catname = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self):
        return self.catname

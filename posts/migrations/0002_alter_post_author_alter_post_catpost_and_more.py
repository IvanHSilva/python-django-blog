# Generated by Django 4.0 on 2022-01-05 19:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('categories', '0003_alter_category_catname'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='catpost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excert',
            field=models.TextField(verbose_name='Excerto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='postimg/%Y/%m/%d', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
    ]

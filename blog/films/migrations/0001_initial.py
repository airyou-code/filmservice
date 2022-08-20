# Generated by Django 4.1 on 2022-08-20 13:15

from django.db import migrations, models
import django.db.models.deletion
import films.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=200)),
                ('angl_name', models.CharField(default='none', max_length=200)),
                ('id_film', models.CharField(default='none', max_length=100)),
                ('img', models.ImageField(default='none', upload_to=films.models.get_image_path, verbose_name='Img')),
                ('url_img', models.CharField(default='none', max_length=300)),
                ('yearProd', models.CharField(default='none', max_length=10)),
                ('country', models.CharField(default='none', max_length=40)),
                ('genre', models.CharField(default='none', max_length=200)),
                ('director', models.CharField(default='none', max_length=100)),
                ('script', models.CharField(default='none', max_length=300)),
                ('producer', models.CharField(default='none', max_length=200)),
                ('Operator', models.CharField(default='none', max_length=200)),
                ('Budget', models.CharField(default='none', max_length=40)),
                ('Fees', models.CharField(default='none', max_length=100)),
                ('premiere', models.CharField(default='none', max_length=40)),
                ('Age', models.CharField(default='none', max_length=40)),
                ('rating', models.CharField(default='none', max_length=40)),
                ('time', models.CharField(default='none', max_length=40)),
                ('description', models.TextField(default='none')),
                ('dateTime', models.DateTimeField(auto_now=True, verbose_name='dateTime')),
                ('tg_age', models.ManyToManyField(to='films.age')),
                ('tg_country', models.ManyToManyField(to='films.country')),
            ],
        ),
        migrations.CreateModel(
            name='Ganer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_persons', models.CharField(max_length=100)),
                ('name', models.CharField(default='none', max_length=200)),
                ('enName', models.CharField(default='none', max_length=200)),
                ('description', models.CharField(default='none', max_length=200)),
                ('enProfession', models.CharField(default='none', max_length=200)),
                ('photo', models.CharField(default='none', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=200)),
                ('img', models.ImageField(default='none', upload_to=films.models.get_image_path, verbose_name='Img')),
                ('description', models.TextField(default='none')),
                ('films', models.ManyToManyField(default='none', to='films.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='tg_genre',
            field=models.ManyToManyField(default='none', to='films.ganer'),
        ),
        migrations.AddField(
            model_name='film',
            name='tg_persons',
            field=models.ManyToManyField(default='none', to='films.persons'),
        ),
        migrations.AddField(
            model_name='film',
            name='tg_type',
            field=models.ManyToManyField(to='films.type'),
        ),
        migrations.AddField(
            model_name='film',
            name='tg_year',
            field=models.ManyToManyField(to='films.year'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='films.film')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_remove_movie_gengere_movie_gengere'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('photo_url', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='slug',
            field=models.SlugField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='null'),
            preserve_default=False,
        ),
    ]

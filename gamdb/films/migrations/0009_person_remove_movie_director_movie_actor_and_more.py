# Generated by Django 4.1.7 on 2023-05-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(blank=True, null=True, related_name='acted', to='films.person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, null=True, related_name='directed', to='films.person'),
        ),
    ]

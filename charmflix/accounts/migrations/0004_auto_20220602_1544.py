# Generated by Django 3.0.14 on 2022-06-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_serie_likes'),
        ('movies', '0008_film_likes'),
        ('accounts', '0003_customer_favoritesseries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='favorites',
            field=models.ManyToManyField(blank=True, to='movies.Film'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='favoritesseries',
            field=models.ManyToManyField(blank=True, to='series.Serie'),
        ),
    ]

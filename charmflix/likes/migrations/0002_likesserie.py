# Generated by Django 3.0.14 on 2022-06-02 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('series', '0002_auto_20220530_1248'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likesserie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serie_post_like', to='series.Serie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serie_user_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

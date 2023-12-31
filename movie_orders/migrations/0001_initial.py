# Generated by Django 4.2 on 2023-04-17 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0003_movieorder_movie_orders'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyed_at', models.DateTimeField()),
                ('price', models.FloatField(max_length=10)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_orders', to='movies.movie')),
                ('user_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_movie_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

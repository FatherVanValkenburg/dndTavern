# Generated by Django 4.1.2 on 2022-10-20 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='age',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='job',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='race',
        ),
        migrations.AddField(
            model_name='hero',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

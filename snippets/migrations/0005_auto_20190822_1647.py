# Generated by Django 2.2.4 on 2019-08-22 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20190822_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
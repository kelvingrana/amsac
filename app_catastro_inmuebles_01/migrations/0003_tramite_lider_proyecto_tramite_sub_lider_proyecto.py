# Generated by Django 5.1.5 on 2025-01-17 22:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_catastro_inmuebles_01', '0002_tramite_receptor_responsable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tramite',
            name='lider_proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lider_proyecto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tramite',
            name='sub_lider_proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_lider_proyecto', to=settings.AUTH_USER_MODEL),
        ),
    ]

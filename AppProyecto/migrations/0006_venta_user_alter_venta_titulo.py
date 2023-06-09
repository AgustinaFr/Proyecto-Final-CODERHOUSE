# Generated by Django 4.1.7 on 2023-03-24 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppProyecto', '0005_remove_venta_user_alter_venta_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venta',
            name='titulo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]

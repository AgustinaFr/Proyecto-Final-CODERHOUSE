# Generated by Django 4.1.7 on 2023-03-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0011_remove_comentarios_vendedor_comentarios_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogo',
            options={'ordering': ['-fecha']},
        ),
        migrations.AddField(
            model_name='catalogo',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
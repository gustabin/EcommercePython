# Generated by Django 4.1.7 on 2023-05-12 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marca', '0005_rename_titulo_marca_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='logo1',
            field=models.ImageField(blank=True, null=True, upload_to='marcas'),
        ),
    ]

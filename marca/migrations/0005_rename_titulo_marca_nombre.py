# Generated by Django 4.1.7 on 2023-05-12 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marca', '0004_rename_empresa_id_marca_empresa_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='titulo',
            new_name='nombre',
        ),
    ]

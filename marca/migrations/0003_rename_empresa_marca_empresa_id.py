# Generated by Django 4.1.7 on 2023-05-11 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marca', '0002_rename_empresa_id_marca_empresa_alter_marca_fecha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='empresa',
            new_name='empresa_Id',
        ),
    ]
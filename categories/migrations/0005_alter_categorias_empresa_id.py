# Generated by Django 4.1.7 on 2023-05-15 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_alter_empresa_direccion_alter_empresa_email_and_more'),
        ('categories', '0004_alter_categorias_empresa_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='empresa_id',
            field=models.ForeignKey(blank=True, default=26, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]

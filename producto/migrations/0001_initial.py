# Generated by Django 4.1.7 on 2023-05-14 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('descripcion', models.TextField()),
                ('especificacion', models.CharField(max_length=3000)),
                ('codigo', models.CharField(max_length=30)),
                ('promocion', models.BooleanField(default=True)),
                ('stock', models.IntegerField()),
                ('orden', models.IntegerField(default=99)),
                ('fecha', models.DateTimeField()),
                ('status', models.IntegerField(default=0)),
                ('calificacion', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.categoria')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.color')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.empresa')),
                ('imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.imagen')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.marca')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.talla')),
            ],
        ),
    ]

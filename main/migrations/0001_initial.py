# Generated by Django 3.1.1 on 2020-09-12 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferencias', models.ManyToManyField(to='main.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reputacion', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distrito', models.CharField(max_length=20)),
                ('provincia', models.CharField(max_length=20)),
                ('departamento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=11)),
                ('razon_social', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_identidad', models.CharField(max_length=8)),
                ('fecha_nacimiento', models.DateField()),
                ('estado', models.CharField(max_length=3)),
                ('genero', models.CharField(choices=[('MA', 'Masculino'), ('FE', 'Femenino'), ('NB', 'No Binario')], max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('estado', models.CharField(max_length=3)),
                ('descuento', models.FloatField(default=0)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.categoria')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(max_length=3)),
                ('direccion_entrega', models.CharField(max_length=100)),
                ('tarifa', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('repatidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.colaborador')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producto')),
            ],
        ),
        migrations.AddField(
            model_name='colaborador',
            name='cobertura_entrega',
            field=models.ManyToManyField(to='main.Localizacion'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
    ]

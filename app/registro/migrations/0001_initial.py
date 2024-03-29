# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=10)),
                ('hora', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inspecciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipios', models.CharField(blank=True, choices=[('Guanare ', 'Guanare'), ('Agua Blanca', 'Agua Blanca'), ('Araure', 'Araure'), ('Esteller', 'Esteller'), ('Guanarito', 'Guanarito'), ('Monseñor Jose Vicente de Unda', 'Monseñor Jose Vicente de Unda'), ('Ospino', 'Ospino'), ('Paez', 'Paez'), ('Papelon', 'Papelon'), ('San Genaro de Boconoito', 'San Genaro de Boconoito'), ('San Rafael de Onoto', 'San Rafael de Onoto'), ('Santa Rosalia', 'Santa Rosalia'), ('Sucre', 'Sucre'), ('Turen', 'Turen')], max_length=200, null=True)),
                ('grep', models.CharField(blank=True, choices=[('Córdoba', 'Córdoba'), ('Guanare', 'Guanare'), ('San José de la Montaña', 'San José de la Montaña'), ('San Juan de Guanaguanare', 'San Juan de Guanaguanare'), ('Virgen de Coromoto', 'Virgen de Coromoto')], max_length=100, null=True)),
                ('aguablancap', models.CharField(blank=True, choices=[('Agua Blanca', 'Agua Blanca')], max_length=100, null=True)),
                ('araurep', models.CharField(blank=True, choices=[('Rio Acarigua', 'Rio Acarigua'), ('araure', 'araure')], max_length=100, null=True)),
                ('estellerp', models.CharField(blank=True, choices=[('Piritu', 'Piritu'), ('Uveral', 'Uveral')], max_length=100, null=True)),
                ('guanaritop', models.CharField(blank=True, choices=[('Guanarito', 'Guanarito'), ('Divina Pastora', 'Divina Pastora'), ('Trinidad de la Capilla', 'Trinidad de la Capilla')], max_length=100, null=True)),
                ('josevicentedeundap', models.CharField(blank=True, choices=[('Peña Blanca', 'Agua Blanca')], max_length=100, null=True)),
                ('ospinop', models.CharField(blank=True, choices=[('Aparicio', 'Aparicio'), ('Estacion', 'Estacion'), ('Ospino', 'Ospino')], max_length=100, null=True)),
                ('paezp', models.CharField(blank=True, choices=[('Aramendi', 'Aramendi'), ('Amparo', 'Amparo'), ('Camilo', 'Camilo'), ('Urbana Guasdualito', 'Urbana Guasdualito'), ('Urdaneta', 'Urdaneta')], max_length=100, null=True)),
                ('papelonp', models.CharField(blank=True, choices=[('Caño Delgadito', 'Caño Delgadito'), ('San Rafael Apóstol de Papelón', 'San Rafael Apóstol de Papelón')], max_length=100, null=True)),
                ('sangenarop', models.CharField(blank=True, choices=[('Antolín Tovar Anquino', 'Antolín Tovar Anquino'), ('Boconoíto', 'Boconoíto')], max_length=100, null=True)),
                ('sanrafaeldeonotop', models.CharField(blank=True, choices=[('Santa Fé', 'Santa Fé'), ('San Rafael de Onoto', 'San Rafael de Onoto'), ('Thermo Morales', 'Thermo Morales')], max_length=100, null=True)),
                ('santarosaliap', models.CharField(blank=True, choices=[('Santa Rosalia', 'Santa Rosalia'), ('Florida', 'Florida')], max_length=100, null=True)),
                ('sucrep', models.CharField(blank=True, choices=[('Sucre', 'Sucre'), ('Concepción', 'Concepción'), ('San José de Saguaz', 'San José de Saguaz'), ('San Rafael de Palo Alzado', 'San Rafael de Palo Alzado'), ('Uvencio Antonio Velásquez', 'Uvencio Antonio Velásquez'), ('Villa Rosa', 'Villa Rosa')], max_length=100, null=True)),
                ('turenp', models.CharField(blank=True, choices=[('Canelones', 'Canelones'), ('Capital Turén', 'Capital Turén'), ('Santa Cruz', 'Santa Cruz')], max_length=100, null=True)),
                ('tlf_habitacion', models.CharField(max_length=12)),
                ('descr_viviendap', models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Rural', 'Rural'), ('Rancho', 'Rancho'), ('Apartamento', 'Apartamento'), ('Quinta', 'Quinta'), ('Barraca', 'Barranca'), ('Tabla', 'Tabla')], max_length=100, null=True)),
                ('tipo_paredp', models.CharField(blank=True, choices=[('Frisada', 'Frisada'), ('Sin Frisada', 'Sin Frisada'), ('Adobe', 'Adobe'), ('Zinc', 'Zinc'), ('Tabla', 'Tabla'), ('Carton', 'Carton'), ('Carton Piedra', 'Carton Piedra')], max_length=100, null=True)),
                ('tipo_pisop', models.CharField(blank=True, choices=[('Cemento', 'Cemento'), ('Rustico', 'Rustico'), ('Tierra', 'Tierra'), ('Balbosa', 'Balbosa'), ('granito', 'granito'), ('Cemento Pulido', 'Cemento Pulido')], max_length=100, null=True)),
                ('tipo_techop', models.CharField(blank=True, choices=[('Aceroli', 'Aceroli'), ('Zinc', 'Zinc'), ('Platabanda', 'Platabanda'), ('Tejas', 'Tejas'), ('Raso', 'Raso'), ('Machembrado', 'Machembrado'), ('Asbesto', 'Asbesto')], max_length=100, null=True)),
                ('tenencia', models.CharField(blank=True, choices=[('Propio', 'Propio'), ('Alquilada', 'Alquilada'), ('Los Padres', 'Los Padres'), ('Prestada', 'Prestada'), ('Hacimaniento', 'hacimaniento')], max_length=100, null=True)),
                ('aseourbano', models.BooleanField()),
                ('electricidad', models.BooleanField()),
                ('aguadepozo', models.BooleanField()),
                ('cloacas', models.BooleanField()),
                ('pozoseptico', models.BooleanField()),
                ('fogon', models.BooleanField()),
                ('gas', models.BooleanField()),
                ('campoabierto', models.BooleanField()),
                ('cisterna', models.BooleanField()),
                ('cita', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Cita')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_oficio', models.IntegerField(blank=True, null=True)),
                ('remitente', models.CharField(blank=True, choices=[('Departamentos de Redes Populares', 'Departamentos de Redes Populares')], max_length=200, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('caso_planteado', models.CharField(max_length=1000)),
                ('tipo_solicitud', models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Alto Riezgo', 'Alto Riezgo'), ('Salud', 'Salud'), ('Institucional', 'Institucional')], max_length=200, null=True)),
                ('adjunto_ci_menor', models.ImageField(upload_to='adjuntado')),
                ('adjunto_constancia_r', models.ImageField(upload_to='adjuntado')),
                ('adjunto_ci', models.ImageField(upload_to='adjuntado')),
                ('adjunto_carnetp', models.ImageField(upload_to='adjuntado')),
                ('adjunto_gmv', models.ImageField(upload_to='adjuntado')),
                ('adjunto_casoriesgo', models.ImageField(blank=True, null=True, upload_to='adjuntado')),
                ('adjunto_informe', models.ImageField(blank=True, null=True, upload_to='adjuntado')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.PUser')),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='solicitud',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Solicitudes'),
        ),
        migrations.AddField(
            model_name='cita',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.PUser'),
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-31 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('core', '0002_pontoturistico_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacao.Localizacao'),
        ),
    ]

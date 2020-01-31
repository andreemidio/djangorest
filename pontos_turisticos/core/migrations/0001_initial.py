# Generated by Django 3.0.2 on 2020-01-31 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localizacao', '0001_initial'),
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=250)),
                ('descricao', models.TextField(blank=True)),
                ('aprovado', models.BooleanField(default=False)),
                ('visivel', models.BooleanField()),
                ('atracoes', models.ManyToManyField(to='atracoes.Atracoes')),
                ('localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localizacao.Localizacao')),
            ],
            options={
                'verbose_name': 'PontoTuristico',
            },
        ),
    ]

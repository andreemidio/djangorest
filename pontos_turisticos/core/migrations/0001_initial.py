# Generated by Django 3.0.2 on 2020-01-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atracoes', '0001_initial'),
        ('comentarios', '0001_initial'),
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
                ('atracoes', models.ManyToManyField(to='atracoes.Atracao')),
                ('comentario', models.ManyToManyField(to='comentarios.Comentario')),
            ],
        ),
    ]

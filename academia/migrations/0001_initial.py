# Generated by Django 3.2.9 on 2021-11-06 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('nascimento', models.DateField(help_text='Formato DD/MM/AAAA', verbose_name='Data Nascimento')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Não Definido', 'Não Definido')], max_length=12, verbose_name='Sexo')),
                ('matricula', models.IntegerField(default='', unique=True, verbose_name='Matrícula')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repeticoes', models.IntegerField(verbose_name='Repetições')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('tipo', models.CharField(max_length=200, verbose_name='Tipo de Treino')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('nascimento', models.DateField(help_text='Formato DD/MM/AAAA', verbose_name='Data Nascimento')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Não Definido', 'Não Definido')], max_length=12, verbose_name='Sexo')),
                ('matricula', models.IntegerField(default='', unique=True, verbose_name='Matrícula')),
                ('descricao', models.TextField(blank=True, max_length=500, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome da Ficha')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='academia.cliente')),
                ('exercicios', models.ManyToManyField(to='academia.Exercicio')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='academia.funcionario')),
            ],
            options={
                'verbose_name': 'Ficha',
                'verbose_name_plural': 'Fichas',
            },
        ),
    ]

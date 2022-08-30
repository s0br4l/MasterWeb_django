# Generated by Django 4.1 on 2022-08-10 01:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_alter_dadospessoais_doenca1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrosdiarios',
            name='observacao',
            field=models.CharField(blank=True, choices=[('OP1', 'Nao fez aula'), ('OP2', 'Nao fez pos'), ('OP3', '1a medida pressao alta'), ('OP4', '1a medida pressao baixa'), ('OP5', '1a medida glicemia alta'), ('OP6', '1a medida glicemia baixa')], max_length=3),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pos_glic1',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pos_glic2',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pos_pad2',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pos_pas2',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pre_glic1',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pre_glic2',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pre_pad2',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pre_pas2',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
    ]
# Generated by Django 4.1 on 2022-08-18 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0005_alter_registrosdiarios_pos_glic1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospessoais',
            name='exames',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='intervencao1',
            field=models.CharField(blank=True, choices=[('HIDRO', 'Hidroginastica'), ('RELAX', 'Relaxamento'), ('PILTS', 'Pilates')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='intervencao2',
            field=models.CharField(blank=True, choices=[('HIDRO', 'Hidroginastica'), ('RELAX', 'Relaxamento'), ('PILTS', 'Pilates')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='turma1',
            field=models.CharField(blank=True, choices=[('TQ7h', 'Terca|Quinta|7h'), ('TQ8h', 'Terca|Quinta|8h'), ('QS7h', 'Quarta|Sexta|7h'), ('QS8h', 'Quarta|Sexta|8h'), ('PILT', 'Pilates')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='turma2',
            field=models.CharField(blank=True, choices=[('TQ7h', 'Terca|Quinta|7h'), ('TQ8h', 'Terca|Quinta|8h'), ('QS7h', 'Quarta|Sexta|7h'), ('QS8h', 'Quarta|Sexta|8h'), ('PILT', 'Pilates')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pos_pad1',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pos_pas1',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pre_pad1',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='registrosdiarios',
            name='pre_pas1',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
    ]
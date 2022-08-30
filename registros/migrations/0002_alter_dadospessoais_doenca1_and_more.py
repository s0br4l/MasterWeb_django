# Generated by Django 4.1 on 2022-08-10 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospessoais',
            name='doenca1',
            field=models.CharField(blank=True, choices=[('HAS', 'Hipertensao'), ('DIB', 'Diabetes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='doenca2',
            field=models.CharField(blank=True, choices=[('HAS', 'Hipertensao'), ('DIB', 'Diabetes')], max_length=3),
        ),
    ]
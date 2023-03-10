# Generated by Django 4.1 on 2022-08-10 00:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPessoais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome usuário')),
                ('turma1', models.CharField(choices=[('TQ7h', 'Terca|Quinta|7h'), ('TQ8h', 'Terca|Quinta|8h'), ('QS7h', 'Quarta|Sexta|7h'), ('QS8h', 'Quarta|Sexta|8h'), ('PILT', 'Pilates')], max_length=4)),
                ('intervencao1', models.CharField(choices=[('HIDRO', 'Hidroginastica'), ('RELAX', 'Relaxamento'), ('PILTS', 'Pilates')], max_length=5)),
                ('turma2', models.CharField(choices=[('TQ7h', 'Terca|Quinta|7h'), ('TQ8h', 'Terca|Quinta|8h'), ('QS7h', 'Quarta|Sexta|7h'), ('QS8h', 'Quarta|Sexta|8h'), ('PILT', 'Pilates')], max_length=4)),
                ('intervencao2', models.CharField(choices=[('HIDRO', 'Hidroginastica'), ('RELAX', 'Relaxamento'), ('PILTS', 'Pilates')], max_length=5)),
                ('exames', models.DateField()),
                ('doenca1', models.CharField(choices=[('HAS', 'Hipertensao'), ('DIB', 'Diabetes')], max_length=3)),
                ('doenca2', models.CharField(choices=[('HAS', 'Hipertensao'), ('DIB', 'Diabetes')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Registrosdiarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervencao', models.CharField(choices=[('HIDRO', 'Hidroginastica'), ('RELAX', 'Relaxamento'), ('PILTS', 'Pilates')], max_length=5)),
                ('data', models.DateField(auto_now=True)),
                ('observacao', models.CharField(choices=[('OP1', 'Nao fez aula'), ('OP2', 'Nao fez pos'), ('OP3', '1a medida pressao alta'), ('OP4', '1a medida pressao baixa'), ('OP5', '1a medida glicemia alta'), ('OP6', '1a medida glicemia baixa')], max_length=3)),
                ('pre_pas1', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pre_pad1', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pre_glic1', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pos_pas1', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pos_pad1', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pos_glic1', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pre_pas2', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pre_pad2', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pre_glic2', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pos_pas2', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pos_pad2', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('pos_glic2', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registros.dadospessoais')),
            ],
        ),
    ]

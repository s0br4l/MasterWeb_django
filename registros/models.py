from django.core.validators import MaxValueValidator
from django.db import models


class DadosPessoais(models.Model):
    TURMAS = (
        ('TQ7h', 'Terca|Quinta|7h'),
        ('TQ8h', 'Terca|Quinta|8h'),
        ('QS7h', 'Quarta|Sexta|7h'),
        ('QS8h', 'Quarta|Sexta|8h'),
        ('PL7h', 'Pilates|7h'),
        ('PL8h', 'Pilates|8h'),
    )

    INTERVENCOES = (
        ('HIDRO', 'Hidroginastica'),
        ('PILTS', 'Pilates'),
    )

    DOENCAS = (
        ('HAS', 'Hipertensao'),
        ('DIB', 'Diabetes'),
    )
    nome = models.CharField('Nome usuário', max_length=250)
    turma1 = models.CharField(max_length=4, choices=TURMAS, blank=True, null=True)
    intervencao1 = models.CharField(max_length=5, choices=INTERVENCOES, blank=True, null=True)
    turma2 = models.CharField(max_length=4, choices=TURMAS, blank=True, null=True)
    intervencao2 = models.CharField(max_length=5, choices=INTERVENCOES, blank=True, null=True)
    exames = models.DateField(blank=True, null=True)
    doenca1 = models.CharField(max_length=3, choices=DOENCAS, blank=True)
    doenca2 = models.CharField(max_length=3, choices=DOENCAS, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.turma1} - {self.turma2}"


class Registrosdiarios(models.Model):
    INTERVENCAO = (
        ('HIDRO', 'Hidroginastica'),
        ('RELAX', 'Relaxamento'),
        ('PILTS', 'Pilates'),
    )
    OBSERVACOES = (
        ('OP1', 'Nao fez aula'),
        ('OP2', 'Nao fez pos'),
        ('OP3', 'Liberada, mesmo com a pressao alterada'),
        ('OP4', 'Liberada, mesmo com a glicemia alterada'),
        ('OP5', '1a medida pressao alta'),
        ('OP6', '1a medida pressao baixa'),
        ('OP7', '1a medida glicemia alta'),
        ('OP8', '1a medida glicemia baixa'),
    )

    nome = models.ForeignKey(DadosPessoais, on_delete=models.PROTECT)
    intervencao = models.CharField(max_length=5, choices=INTERVENCAO, blank=True)
    data = models.DateField(auto_now=True)
    observacao = models.CharField(max_length=3, choices=OBSERVACOES, blank=True)
    pre_pas1 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pre_pad1 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pre_glic1 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pos_pas1 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pos_pad1 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pos_glic1 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pre_pas2 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pre_pad2 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pre_glic2 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pos_pas2 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pos_pad2 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)
    pos_glic2 = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank=True, null=True)

    def __str__(self):
        return str(f"{self.data} - {self.nome}")

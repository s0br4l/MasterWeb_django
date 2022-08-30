from django import forms
from django.db.models import Q
from django.forms import ModelForm
from .models import DadosPessoais, Registrosdiarios


class CadastroForm(ModelForm):

    class Meta:

        model = DadosPessoais
        fields = ('nome', 'turma1', 'intervencao1', 'turma2', 'intervencao2', 'exames', 'doenca1', 'doenca2')
        labels = {
            'nome': 'Nome completo ',
            'turma1': 'Selecione a turma 1 ',
            'intervencao1': 'Selecione a intervencao da turma 1 ',
            'turma2': 'Selecione a turma 2 ',
            'intervencao2': 'Selecione a intervencao da turma 2 ',
            'exames': 'Data de vencimento dos exames (M/D/A) ',
            'doenca1': 'Selecione se tem doencas ',
            'doenca2': 'Selecione se tem doencas ',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Como consta no documento'}),
            'turma1': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'intervencao1': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'turma2': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'intervencao2': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'exames': forms.SelectDateWidget(empty_label=("Ano", "Mês", "Dia"),
                                             attrs={'class': 'form-select'}),
            'doenca1': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'doenca2': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
        }


class PressaoPreForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PressaoPreForm, self).__init__(*args, **kwargs)
        self.fields['nome'].queryset = DadosPessoais.objects.all().order_by('nome')

    class Meta:
        model = Registrosdiarios
        fields = ('nome', 'intervencao', 'observacao', 'pre_pas1', 'pre_pad1', 'pre_pas2', 'pre_pad2')
        labels = {
            'nome': 'Selecione o nome para registrar ',
            'intervencao': ' Selecione a intervencao do dia ',
            'observacao': ' Observacoes (preencha caso algo ocorra) ',
            'pre_pas1': ' 1a medida Pré da PAS ',
            'pre_pad1': ' 1a medida Pré PAD ',
            'pre_pas2': ' 2a medida Pré PAS ',
            'pre_pad2': ' 2a medida Pré PAD ',
        }

        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'intervencao': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'observacao': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'pre_pas1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 123'}),
            'pre_pad1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 78'}),
            'pre_pas2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(caso necessário, e justificar nas observacoes)'}),
            'pre_pad2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(caso necessário, e justificar nas observacoes)'}),

        }


class PressaoPosForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PressaoPosForm, self).__init__(*args, **kwargs)
        self.fields['nome'].queryset = DadosPessoais.objects.all().order_by('nome')

    class Meta:
        model = Registrosdiarios
        fields = ('nome', 'intervencao', 'observacao', 'pos_pas1', 'pos_pad1', 'pos_pas2', 'pos_pad2')
        labels = {
            'nome': 'Selecione o nome para registrar ',
            'intervencao': ' Selecione a intervencao do dia ',
            'observacao': ' Observacoes (preencha caso algo ocorra) ',
            'pos_pas1': ' 1a medida Pós da PAS ',
            'pos_pad1': ' 1a medida Pós da PAD ',
            'pos_pas2': ' 2a medida Pós da PAS ',
            'pos_pad2': ' 2a medida Pós da PAD ',
        }

        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'intervencao': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'observacao': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'pos_pas1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 123'}),
            'pos_pad1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 78'}),
            'pos_pas2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(caso necessário, e justificar nas observacoes)'}),
            'pos_pad2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(caso necessário, e justificar nas observacoes)'}),

        }


class GlicemiaPreForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GlicemiaPreForm, self).__init__(*args, **kwargs)
        self.fields['nome'].queryset = DadosPessoais.objects.filter(Q(doenca1='DIB') | Q(doenca2='DIB')).order_by('nome')

    class Meta:
        model = Registrosdiarios
        fields = ('nome', 'intervencao', 'observacao', 'pre_glic1', 'pre_glic2')
        labels = {
            'nome': 'Selecione o nome para registrar ',
            'intervencao': ' Selecione a intervencao do dia ',
            'observacao': ' Observacoes (preencha caso algo ocorra) ',
            'pre_glic1': ' 1a medida Pré da Glicemia ',
            'pre_glic2': ' 2a medida Pré da Glicemia ',

        }

        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'intervencao': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'observacao': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'pre_glic1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(caso necessário, e justificar nas observacoes)'}),
            'pre_glic2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(caso necessário, e justificar nas observacoes)'}),
        }


class GlicemiaPosForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GlicemiaPosForm, self).__init__(*args, **kwargs)
        self.fields['nome'].queryset = DadosPessoais.objects.filter(Q(doenca1='DIB') | Q(doenca2='DIB')).order_by('nome')

    class Meta:

        model = Registrosdiarios
        fields = ('nome', 'intervencao', 'observacao', 'pos_glic1', 'pos_glic2')
        labels = {
            'nome': 'Selecione o nome para registrar ',
            'intervencao': ' Selecione a intervencao do dia ',
            'observacao': ' Observacoes (preencha caso algo ocorra) ',
            'pos_glic1': ' 1a medida Pós da Glicemia ',
            'pos_glic2': ' 2a medida Pós da Glicemia ',
        }

        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'intervencao': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'observacao': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'pos_glic1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(caso necessário, e justificar nas observacoes)'}),
            'pos_glic2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(caso necessário, e justificar nas observacoes)'}),
        }



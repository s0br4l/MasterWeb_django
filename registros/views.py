import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import DadosPessoais, Registrosdiarios
from .forms import CadastroForm, PressaoPreForm, PressaoPosForm, GlicemiaPreForm, GlicemiaPosForm
import plotly.graph_objects as go


def home(request):
    return render(request, 'home.html', {})


def newuser(request):
    submitted = False
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newuser?submitted=True')
    else:
        form = CadastroForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'newuser.html', {'form': form, 'submitted': submitted})


def lista_pressao(request):
    lista_pressao = DadosPessoais.objects.all().order_by('nome')
    datahoje = datetime.datetime.now().strftime("%A | %d/%m/%Y | %H:%M:%S")
    datacheck = datetime.date.today()
    lista_dia = Registrosdiarios.objects.filter(data=datacheck)
    lista_dia_pre = set()
    lista_dia_pos = set()
    for user in lista_dia:
        if user.pre_pas1:
            lista_dia_pre.add(user.nome_id)

    for user in lista_dia:
        if user.pos_pas1:
            lista_dia_pos.add(user.nome_id)


    return render(request, 'lista_pressao.html', {
        'lista_pressao': lista_pressao, 'datahoje': datahoje, 'datacheck': datacheck,
    'lista_dia_pre': lista_dia_pre, 'lista_dia_pos': lista_dia_pos})


def lista_glicemia(request):
    lista_glicemia = DadosPessoais.objects.filter(Q(doenca1='DIB') | Q(doenca2='DIB')).order_by('nome')
    datahoje = datetime.datetime.now().strftime("%A | %d/%m/%Y | %H:%M:%S")
    datacheck = datetime.date.today()
    lista_dia = Registrosdiarios.objects.filter(data=datacheck)
    lista_dia_pre = set()
    lista_dia_pos = set()
    for user in lista_dia:
        if user.pre_glic1:
            lista_dia_pre.add(user.nome_id)

    for user in lista_dia:
        if user.pos_glic1:
            lista_dia_pos.add(user.nome_id)

    return render(request, 'lista_glicemia.html', {
        'lista_glicemia': lista_glicemia, 'datahoje': datahoje, 'datacheck': datacheck,
    'lista_dia_pre': lista_dia_pre, 'lista_dia_pos': lista_dia_pos})


def registro_pressao_pre(request):
    submitted = False
    if request.method == "POST":
        form = PressaoPreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registro_pressao_pre?submitted=True')
    else:
        form = PressaoPreForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'registro_pressao_pre.html', {'form': form, 'submitted': submitted})


def registro_pressao_pos(request):
    submitted = False
    if request.method == "POST":
        form = PressaoPosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registro_pressao_pos?submitted=True')
    else:
        form = PressaoPosForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'registro_pressao_pos.html', {'form': form, 'submitted': submitted})


def registro_glic_pre(request):
    submitted = False
    if request.method == "POST":
        form = GlicemiaPreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registro_glic_pre?submitted=True')
    else:
        form = GlicemiaPreForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'registro_glic_pre.html', {'form': form, 'submitted': submitted})


def registro_glic_pos(request):
    submitted = False
    if request.method == "POST":
        form = GlicemiaPosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registro_glic_pos?submitted=True')
    else:
        form = GlicemiaPosForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'registro_glic_pos.html', {'form': form, 'submitted': submitted})


def usuarios_graf(request, user_id):
    usuarios = Registrosdiarios.objects.filter(nome_id=user_id).order_by('-data')[:30]

    figpas = go.Figure(data=[
        go.Bar(name='Pré', x=[u.data for u in usuarios], y=[u.pre_pas1 for u in usuarios]),
        go.Bar(name='Pós', x=[u.data for u in usuarios], y=[u.pos_pas1 for u in usuarios])
    ])
    figpad = go.Figure(data=[
        go.Bar(name='Pré', x=[u.data for u in usuarios], y=[u.pre_pad1 for u in usuarios]),
        go.Bar(name='Pós', x=[u.data for u in usuarios], y=[u.pos_pad1 for u in usuarios])
    ])

    figpas.update_layout(barmode='group',
                         title={'text': 'Pressão arterial sistólica (PAS)', 'xanchor': 'center', 'x': 0.5,
                                'font': {'size': 22}},
                         xaxis={'title': 'Datas', 'titlefont': {'size': 18}},
                         yaxis={'title': 'PAS (mmHg)', 'titlefont': {'size': 18}, 'range': (100, 160)})

    figpad.update_layout(barmode='group',
                         title={'text': 'Pressão arterial diastólica (PAD)', 'xanchor': 'center', 'x': 0.5,
                                'font': {'size': 22}},
                         xaxis={'title': 'Datas', 'titlefont': {'size': 18}},
                         yaxis={'title': 'PAD (mmHg)', 'titlefont': {'size': 18}, 'range': (50, 100)})
    grafpas = figpas.to_html()
    grafpad = figpad.to_html()

    return render(request, 'usuarios_graf.html', {
        'usuarios': usuarios, 'grafpas': grafpas, 'grafpad': grafpad})


def usuarios(request, user_id):
    usuarios = DadosPessoais.objects.get(pk=user_id)

    return render(request, 'usuarios.html', {
        'usuarios': usuarios})


def usuariosedit(request, user_id):
    usuariosedit = DadosPessoais.objects.get(pk=user_id)
    form = CadastroForm(request.POST or None, instance=usuariosedit)
    if form.is_valid():
        form.save()
        messages.success(request, ("Cadastro atualizado"))
        return redirect('usuarios', user_id)

    return render(request, 'edituser.html', {
        'usuariosedit': usuariosedit, 'form': form})



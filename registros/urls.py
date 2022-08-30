from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('newuser', views.newuser, name='newuser'),
   path('usuarios_graf/<user_id>', views.usuarios_graf, name='usuarios_graf'),
   path('usuarios/<user_id>', views.usuarios, name='usuarios'),
   path('usuariosedit/<user_id>', views.usuariosedit, name='usuariosedit'),
   path('lista_pressao', views.lista_pressao, name='lista_pressao'),
   path('lista_glicemia', views.lista_glicemia, name='lista_glicemia'),
   path('registro_pressao_pre', views.registro_pressao_pre, name='registro_pressao_pre'),
   path('registro_pressao_pos', views.registro_pressao_pos, name='registro_pressao_pos'),
   path('registro_glic_pre', views.registro_glic_pre, name='registro_glic_pre'),
   path('registro_glic_pos', views.registro_glic_pos, name='registro_glic_pos'),

]

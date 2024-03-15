from django.contrib import admin
from django.urls import path
from cadastro_app import views
from usuarios import views as usuario_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('', views.visitantes, name='visitantes'),
    path('cadastro/', views.criar, name='novo_visitante'),
    path('editar/<int:id_visitante>', views.editar, name='editar'),
    path('excluir/<int:id_visitante>', views.excluir, name='excluir'),
    path('detalhes/<int:id_visitante>', views.detalhe, name='detalhe'),
    path('permissao_negada/', views.permissao_negada, name='permissao_negada')
]

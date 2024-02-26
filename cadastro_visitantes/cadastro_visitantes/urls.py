from django.contrib import admin
from django.urls import path
from cadastro_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.visitantes, name='visitantes'),
    path('cadastro/', views.criar, name='novo_visitante'),
    path('editar/<int:id_visitante>', views.editar, name='editar'),
    path ('detalhes/<int:id_visitante>', views.detalhe, name='detalhe')
]

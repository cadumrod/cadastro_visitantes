from django.contrib import admin
from django.urls import path
from cadastro_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.visitantes, name='visitantes'),
    path('cadastro/', views.criar, name='novo_visitante'),
    path('cadastro/<int:id_visitante>', views.editar, name='editar'),
    path ('/<int:id_visitante>', views.detalhe, name='detalhe')
]

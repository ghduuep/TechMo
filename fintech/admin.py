from django.contrib import admin
from fintech.models import Categoria, Transacao

class TransacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'valor', 'tipo', 'categoria']
    list_display_links = ['id', 'usuario', 'categoria']
    list_per_page = 20
    search_fields = ['id', 'usuario', 'tipo', 'categoria']
    list_filter = ['usuario', 'tipo', 'categoria']

admin.site.register(Transacao, TransacaoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao']
    list_display_links = ['id', 'nome', 'descricao']
    search_fields = ['id', 'nome', 'descricao']
    list_filter = ['nome', 'descricao']

admin.site.register(Categoria, CategoriaAdmin)




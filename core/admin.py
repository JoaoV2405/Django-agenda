from django.contrib import admin

from core.models import Evento

# Register your models here.
class Evento_Admin(admin.ModelAdmin):
    #faz essas opçoes aparecerem na tabela
    list_display = ('titulo', 'data_criacao', 'data_evento')
    list_filter = ('titulo', )



admin.site.register(Evento, Evento_Admin)
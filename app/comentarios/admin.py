from django.contrib import admin
from app.comentarios.models import Comentarios

@admin.register(Comentarios)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("post_id", "autor", "fecha", "estado")
    list_filter = ("post_id", "autor", "estado")
    search_fields = ("autor", "cuerpo")
from django.contrib import admin
from .models import Vinilo, Cassette, Cd

# Register your models here.

class ViniloAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "fecha_lanzamiento"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["nuevo"]
    list_per_page = 10

admin.site.register(Vinilo, ViniloAdmin)

class CasseteAdmin(admin.ModelAdmin):
    list_display = ["nombre_cassete", "precio_cassete", "nuevo_cassete", "fecha_lanzamiento_cassete"]
    list_editable = ["precio_cassete"]
    search_fields = ["nombre_cassete"]
    list_filter = ["nuevo_cassete"]
    list_per_page = 10

admin.site.register(Cassette, CasseteAdmin)

class CdsAdmin(admin.ModelAdmin):
    list_display = ["nombre_cd", "precio_cd", "nuevo_cd", "fecha_lanzamiento_cd"]
    list_editable = ["precio_cd"]
    search_fields = ["nombre_cd"]
    list_filter = ["nuevo_cd"]
    list_per_page = 10

admin.site.register(Cd, CdsAdmin)
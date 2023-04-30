from django.contrib import admin

from .models import Empleado,Habilidades,Departamento

admin.site.register(Departamento)
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'job'
    )

admin.site.register(Empleado, EmpleadoAdmin)

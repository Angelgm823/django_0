from django.contrib import admin
from .models import Autor,Libros, DetallesLibro, Prestamo, Critica, Genero
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

User = get_user_model()

@admin.action(description='Marcar prestamos como devueltos')
def marcar_regreso(modeladmin, request, queryset):
    queryset.update(estado=True)

class PrestamoEnLinea(admin.TabularInline):
    model= Prestamo
    extra=1

class CriticaEnLinea(admin.TabularInline):
    model= Critica
    extra= 1

class DetalleLibroEnLinea(admin.StackedInline):
    model = DetallesLibro
    can_delete = False

class CustomUserAdmin(BaseUserAdmin):
    inlines= [PrestamoEnLinea]
    list_display = ('username', 'email')


@admin.register(Libros)
class LibroAdmin(admin.ModelAdmin):
    inlines = [CriticaEnLinea, DetalleLibroEnLinea]
    list_display = ('titulo', 'autor', 'paginas', 'fecha_publicacion')
    search_fields = ('titulo', 'autor__nombre')
    list_filter = ('autor', 'generos', 'fecha_publicacion')
    ordering = ['fecha_publicacion']
    date_hierarchy = 'fecha_publicacion'

    readonly_fields = ('paginas', 'isbn',)

    fieldsets=(
        ('Informacion general',{
            'fields': ('titulo', 'autor', 'fecha_publicacion', 'generos')
        }),
        ('Detalles',{
            'fields':('isbn', 'paginas'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_ingreso',)
    list_display= ('usuario', 'libro', 'fecha_ingreso' ,'estado')
    actions=[marcar_regreso]


admin.site.register(Autor)
#admin.site.register(Libros, LibroAdmin)
#admin.site.register(Prestamo)
admin.site.register(DetallesLibro)
admin.site.register(Critica)
admin.site.register(Genero)

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(User, CustomUserAdmin)
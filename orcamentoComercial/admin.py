from django.contrib import admin
from .forms import OrcamentoComercialForm
from .models import OrcamentoComercial, Cargo, Senioridade, Pagamento, Area

@admin.register(OrcamentoComercial)
class OrcamentoComercialAdmin(admin.ModelAdmin):
    form = OrcamentoComercialForm
    list_display = ('area', 'cargo','forma_pagamento', 'margem')
    list_filter = ('area', 'cargo','forma_pagamento')
    search_fields = ('area', 'cargo','forma_pagamento')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'senioridade','salario')


@admin.register(Senioridade)
class SenioridadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome',)



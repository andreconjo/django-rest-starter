from django.contrib import admin
from .forms import OrcamentoComercialForm
from .models import OrcamentoComercial, Cargo

@admin.register(OrcamentoComercial)
class OrcamentoComercialAdmin(admin.ModelAdmin):
    form = OrcamentoComercialForm
    list_display = ('area', 'cargo','forma_pagamento', 'margem')
    list_filter = ('area', 'cargo','forma_pagamento')
    search_fields = ('area', 'cargo','forma_pagamento')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'senioridade','salario')


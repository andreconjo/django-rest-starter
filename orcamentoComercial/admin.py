from django.contrib import admin
from .forms import OrcamentoComercialForm
from .models import OrcamentoComercial

@admin.register(OrcamentoComercial)
class OrcamentoComercialAdmin(admin.ModelAdmin):
    form = OrcamentoComercialForm
    list_display = ('area', 'profissional', 'senioridade', 'forma_pagamento', 'margem')
    list_filter = ('area', 'profissional', 'senioridade', 'forma_pagamento')
    search_fields = ('area', 'profissional', 'senioridade', 'forma_pagamento')


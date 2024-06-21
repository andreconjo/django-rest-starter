from django.contrib import admin
from .models import OrcamentoComercial
from .forms import OrcamentoComercialForm

@admin.register(OrcamentoComercial)
class OrcamentoComercialAdmin(admin.ModelAdmin):
    form = OrcamentoComercialForm
    list_display = ('area', 'profissional', 'senioridade', 'forma_pagamento', 'margem')
    list_filter = ('area', 'profissional', 'senioridade', 'forma_pagamento')
    search_fields = ('area', 'profissional', 'senioridade', 'forma_pagamento')

from django.db import models

class OrcamentoComercial(models.Model):
    AREA_CHOICES = [
        ('analytics', 'Analytics'),
        ('desenvolvimento', 'Desenvolvimento'),
        ('gestao', 'Gestão'),
    ]

    PROFISSIONAL_CHOICES = [
        ('desenvolvedor', 'Desenvolvedor'),
        ('analista_dados', 'Analista de Dados'),
        # Adicione outras opções conforme necessário
    ]

    SENIORIDADE_CHOICES = [
        ('junior', 'Junior'),
        ('pleno', 'Pleno'),
        ('senior', 'Senior'),
        ('especialista', 'Especialista'),
        ('coordenador', 'Coordenador'),
        ('tech_lead', 'Tech Lead'),
    ]

    FORMA_PAGAMENTO_CHOICES = [
        ('pre_pago', 'Pré Pago'),
        ('30_dias', '30 dias'),
        ('60_dias', '60 dias'),
        ('90_dias', '90 dias'),
    ]

    area = models.CharField(max_length=50, choices=AREA_CHOICES)
    profissional = models.CharField(max_length=50, choices=PROFISSIONAL_CHOICES)
    senioridade = models.CharField(max_length=50, choices=SENIORIDADE_CHOICES)
    forma_pagamento = models.CharField(max_length=50, choices=FORMA_PAGAMENTO_CHOICES)
    margem = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)

    def __str__(self):
        return f"{self.area} - {self.profissional} - {self.senioridade}"



from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length=40)
    senioridade = models.CharField(max_length=40)
    salario = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nome}"

class OrcamentoComercial(models.Model):
    AREA_CHOICES = [
        ('analytics', 'Analytics'),
        ('desenvolvimento', 'Desenvolvimento'),
        ('gestao', 'Gestão'),
    ]

    #PROFISSIONAL_CHOICES = [
    #    ('desenvolvedor', 'Desenvolvedor'),
    #    ('analista_dados', 'Analista de Dados'),
    #]

    #SENIORIDADE_CHOICES = [
    #    ('junior', 'Junior'),
    #    ('pleno', 'Pleno'),
    #    ('senior', 'Senior'),
    #    ('especialista', 'Especialista'),
    #    ('coordenador', 'Coordenador'),
    #    ('tech_lead', 'Tech Lead'),
    #]

    FORMA_PAGAMENTO_CHOICES = [
        ('pre_pago', 'Pré Pago'),
        ('30_dias', '30 dias'),
        ('60_dias', '60 dias'),
        ('90_dias', '90 dias'),
    ]

    area = models.CharField(max_length=40, choices=AREA_CHOICES)
    cargo = models.ForeignKey(Cargo, on_delete=models.DO_NOTHING)
    forma_pagamento = models.CharField(max_length=40, choices=FORMA_PAGAMENTO_CHOICES)
    margem = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)

    def __str__(self):
        return f"{self.area} - {self.cargo} - {self.cargo.nome}"



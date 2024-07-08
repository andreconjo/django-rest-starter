from django.db import models

class Area(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nome}"

class Pagamento(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nome}"

class Senioridade(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nome}"

class Cargo(models.Model):
    nome = models.CharField(max_length=40)
    senioridade = models.ForeignKey(Senioridade, on_delete=models.CASCADE)
    salario = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nome}"

class OrcamentoComercial(models.Model):

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    margem = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)

    def __str__(self):
        return f"{self.area} - {self.cargo} - {self.cargo.nome}"



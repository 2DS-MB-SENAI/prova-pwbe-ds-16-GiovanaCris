from django.db import models

class Medico (models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    escolha_especialidade = (
        ('CAR', 'CAR'), #Catdiologista
        ('NEU', 'NEU'), #Neurologista
        ('PSI', 'PSI'), #Psiquiatra
    )
    especialidade = models.CharField(max_length=255, choices=escolha_especialidade)

    def __str__(self):
        return self.nome
    
class Consulta (models.Model):
    paciente = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status_escolha = (
        ('gendado', 'Agendado'),
        ('Realizado', 'Realizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField(max_length=255, choices=status_escolha)

    def __str__(self):
        return self.paciente
from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

# class DetalhesConsulta(forms.Form):
#     paciente = forms.CharField(required=False, label='Nome do paciente: ')
#     data = forms.DateTimeField(required=False, label= 'Data da consulta: ')
#     medico = forms.CharField(required=False, label= 'Nome do meidco da consulta: ')
#     status = forms.CharField(required=False, label= 'Status da consulta: ')

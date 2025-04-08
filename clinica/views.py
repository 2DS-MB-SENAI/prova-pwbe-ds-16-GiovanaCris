from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsultaForm
from .models import Consulta, Medico

def listar_medicos(request):
    medico = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medico': medico})

def criar_consulta(request):
    if request.method == 'POST':
        listform = ConsultaForm(request.POST)
        if listform.is_valid():
            listform.save()

    else:
        listform = ConsultaForm()
    return render(request, 'criar_consulta.html', {'medico': listform})

def detalhes_consulta(request, pk):
    detalhes = get_object_or_404(Consulta, pk=pk)
    if request.method == 'GET':
        form = ConsultaForm(request.GET, instance=detalhes)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas.html')

# def detalhes_consulta(request):
#     consulta = Consulta.objects.all()

#     paciente = request.GET.get('paciente', '')
#     data = request.GET.get('data', '')
#     medico = request.GET.get('medico', '')
#     status = request.GET.get('status', '')

#     if paciente:
#         consulta = consulta.filter(paciente__icontains=paciente)

#     if data:
#         consulta = consulta.filter(data__icontains=data)

#     if medico:
#         consulta = consulta.filter(medico__icontains=medico)

#     if status:
#         consulta = consulta.filter(status__icontains=status)

#     return render(request, 'criar_consulta.html', {
#         'paciente': paciente,
#         'data': data,
#         'medico': medico,
#         'status': status,
#     })
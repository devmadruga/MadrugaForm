from .models import Paciente
from django.views.generic import CreateView, DetailView


class PacienteCreate(CreateView):
    """
    As CreatView esperam encontrar um template com nome 'model_form.html'.
    Como o nome do model é Paciente, ela espera 'paciente_form.html'.
    Nota que depois de cadastrar, serei redirecionado, por default,
    para uma página (DetailView). Se eu não criar ela, dará um erro 
    de redirecionamento. Também posso definir uma página de redirecionamento
    utilizando o success_url...
    """
    model = Paciente
    fields = '__all__'

    # sucess_url = 'aqui teria que ir uma url'

class PacienteDetail(DetailView):
    """
    As DetailView esperam encontrar um template com nome 'model_detail.html'.
    Como o nome do model é Paciente, ela espera 'paciente_detail.html'.
    """
    model = Paciente
    
from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formulariopacientes import Formularipaciente

from web.models import Medicos

from web.models import Pacientes


# Create your views here.
# renderizar es PINTAR
def Home(request):
    return render(request,'index.html')


def consultoriomedico(request):
    medicosConsultados=Medicos.objects.all()
    datosMedicos={
        "medicos":medicosConsultados


    }
    return render (request,'consultoriomedico.html',datosMedicos)


def consultoriopacientes(request):
    pacientesconsulta=Pacientes.objects.all()
    datospaciente={
        "pacientes":pacientesconsulta
    }
    return render (request,'pacientes2.html',datospaciente)



def MedicosVista(request):
    #creamos una variable para controlar la
    #ejec de la alerta
    lanzandoAlerta=False

    #Debo utilizar la clase formularioMedico
    #CREAMOS ASI UN OBJETO
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario,
        "bandera":lanzandoAlerta
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
            #LLevar mis datos hacia la BD
            medicoNuevo=Medicos(
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tarjeta=datos["tarjetaProfesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"]
            )
            medicoNuevo.save()
            diccionario["bandera"]=True
           


    return render(request,'registromedicos.html',diccionario)

    
def PacienteVista(request):

    #Debo utilizar la clase formularioMedico
    #CREAMOS ASI UN OBJETO
    formulario=Formularipaciente()
    diccionario={
        "formulario":formulario
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=Formularipaciente(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
             #llevar mis datos hacia la BD
            PacienteNuevo=Pacientes(
                nombrepaciente=datos["nombrepaciente"],
                apellidospaciente=datos["apellidosPaciente"],
                cedulapaciente=datos["cedulaPaciente"],
                tipoafiliado=datos["TipoAfiliado"],
                regimen=datos["Regimen"],
                grupo_ingresos=datos["Grupo_ingresos"]
               
           )
            PacienteNuevo.save()
            print("Exito ")
    return render(request,'Pacientes.html',diccionario)
     


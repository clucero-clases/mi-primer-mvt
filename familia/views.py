from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms import PersonaForm, BuscarPersonasForm, DomicilioForm, LaboralForm

from familia.models import Persona, Domicilio, Laboral

def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})

def borrarRelacion(tabla, identificador):
    items = tabla.objects.filter(idPersona=int(identificador))
    if(items.count()>0):
        items.delete()

def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        borrarRelacion(Laboral, identificador)
        borrarRelacion(Domicilio, identificador)
        
        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)

        return render(request, 'familia/lista_familiares.html', {"personas": personas})

def domicilio(request, identificador):
    if request.method == "POST":
        form = DomicilioForm(request.POST)
        if form.is_valid():
            calle = form.cleaned_data['calle']
            numero = form.cleaned_data['numero']
            ciudad = form.cleaned_data['ciudad']
            provincia = form.cleaned_data['provincia']
            
            borrarRelacion(Domicilio, identificador)
            Domicilio(idPersona=identificador, calle=calle, numero=numero, ciudad=ciudad, provincia=provincia).save()
            return HttpResponseRedirect("/")

    elif request.method == "GET":
        domicilio = Domicilio.objects.filter(idPersona=identificador).last()
        if(domicilio):
            form = DomicilioForm(initial={'calle':domicilio.calle, 'numero':domicilio.numero, 'ciudad':domicilio.ciudad, 'provincia':domicilio.provincia})
        else:
            form = DomicilioForm()

        return render(request, 'familia/form_domicilio.html', {'form': form, 'idPersona':identificador})


def laboral(request, identificador):
    if request.method == "POST":
        form = LaboralForm(request.POST)
        if form.is_valid():
            actividad = form.cleaned_data['actividad']
            antiguedad = form.cleaned_data['antiguedad']
            borrarRelacion(Laboral, identificador)
            Laboral(idPersona=identificador, actividad=actividad, antiguedad=antiguedad).save()
            return HttpResponseRedirect("/")

    elif request.method == "GET":
        laboral = Laboral.objects.filter(idPersona__icontains=identificador).last()
        if(laboral):
            form = LaboralForm(initial={'actividad':laboral.actividad, 'antiguedad':laboral.antiguedad})
        else:
            form = LaboralForm()

        return render(request, 'familia/form_laboral.html', {'form': form, 'idPersona':identificador })

    
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import relay_functions
from module_1.models import Luz, Puerta, Habitacion, Sanitario, Alarma, Usuario
from django.contrib.auth import authenticate
import time
from omnibus.factories import websocket_connection_factory
from omnibus.api import publish
# Create your views here.

def index(request):
    if request.user.is_authenticated():
        context = RequestContext(request)
        luces = Luz.objects.all()
        puertas = Puerta.objects.all()
        habitaciones = Habitacion.objects.all()
        sanitarios = Sanitario.objects.all()
        alarmas = Alarma.objects.all()
        for luz in luces:
            luz_aux= Luz.objects.get(id = luz.id)
            luz_aux.status = relay_functions.getStatus(luz.pin)
            luz_aux.save()
        for puerta in puertas:
            puerta_aux= Puerta.objects.get(id = puerta.id)
            puerta_aux.status = relay_functions.getStatus(puerta.pin)
            puerta_aux.save()
        for alarma in luces:
            alarma_aux= Luz.objects.get(id = alarma.id)
            alarma_aux.status = relay_functions.getStatus(alarma.pin)
            alarma_aux.save()

        luces = Luz.objects.all()
        puertas = Puerta.objects.all()
        habitaciones = Habitacion.objects.all()
        sanitarios = Sanitario.objects.all()
        alarmas = Alarma.objects.all()

        return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)
    else:
        context = RequestContext(request)
        return render_to_response('login.html',
                              context)

def luz(request):
    context = RequestContext(request)
    id= request.POST.get('id')
    lista_permitidos = Usuario.objects.filter(permisos_luces=id)
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                luz = Luz.objects.get(id = id)
                if luz.status:
                    luz.status=False
                    relay_functions.relay("close",luz.pin)
                else:
                    luz.status=True
                    relay_functions.relay("open",luz.pin)
                luz.save()
    luces = Luz.objects.all()
    """for luz in luces:
            luz_aux= Luz.objects.get(id = luz.id)
            luz_aux.status = relay_functions.getStatus(luz.pin)
            luz_aux.save()

    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)"""
    return render_to_response('luces.html',{'luz':luz}, context)


def puerta(request):
    context = RequestContext(request)
    id= request.POST.get('id')
    puerta = Puerta.objects.get(id = id)
    lista_permitidos = Usuario.objects.filter(permisos_puertas=id)
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                if puerta.status:
                    puerta.status = False
                    print puerta.status
                    relay_functions.relay("close",puerta.pin)
                else:
                    puerta.status = True
                    relay_functions.relay("open",puerta.pin)
                puerta.save()
                print puerta.status
    puertas = Puerta.objects.all()
    """for puerta in puertas:
            puerta_aux= Puerta.objects.get(id = puerta.id)
            puerta_aux.status = relay_functions.getStatus(puerta.pin)
            print puerta_aux.status
            puerta_aux.save()
    puertas = Puerta.objects.all()
    luces = Luz.objects.all()

    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)"""
    return render_to_response('puertas.html',{'puerta':puerta}, context)

def sanitario(request, id_sanitario):
    context = RequestContext(request)
    sanitario = Sanitario.objects.get(id = id_sanitario)
    if sanitario.ocupado:
        sanitario.ocupado = False
    else:
        sanitario.ocupado = True
    sanitario.save()
    """luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)"""
    return redirect('/')


def habitacion(request):
    context = RequestContext(request)
    id= request.POST.get('id')
    lista_permitidos = Usuario.objects.filter(permisos_habitaciones=id)
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                print "TRUEEE"
                habitacion = Habitacion.objects.get(id = id)
                luces = Luz.objects.filter(lugar_id = id)
                if habitacion.status:
                    habitacion.status = False
                    for luz in luces:
                        relay_functions.relay("close",luz.pin)
                        luz.status = habitacion.status
                        luz.save()
                else:
                    habitacion.status = True
                    for luz in luces:
                        relay_functions.relay("open",luz.pin)
                        luz.status = habitacion.status
                        luz.save()
    habitacion.save()
    habitaciones = Habitacion.objects.all()
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    return render_to_response('habitaciones.html',{'luces':luces,'puertas':puertas,'habitaciones':habitaciones}, context)

def hab_get(request):
    context = RequestContext(request)
    habitaciones = Habitacion.objects.all()
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    return render_to_response('habitaciones.html',{'luces':luces,'puertas':puertas,'habitaciones':habitaciones}, context)

def alarma(request, id_alarma):
    context = RequestContext(request)
    ## Codigo para que suene la chichasha
    ##
    alarma = Alarma.objects.get(id = id_alarma)
    if alarma.status:
        relay_functions.relay("close",alarma.pin)
        alarma.status=False
    else:
        relay_functions.relay("open",alarma.pin)
        alarma.status=True
    alarma.save()
    """luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)"""
    return redirect("/")

@requires_csrf_token
def login_user(request):

    context = RequestContext(request)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = RequestContext(request)
                return redirect("/")
            else:
                context = RequestContext(request)
                return render_to_response('login.html',
                              context)
        else:
            context = RequestContext(request)
            return render_to_response('login.html',
                              context)
    else:
        context = RequestContext(request)
        return render_to_response('login.html',
                              context)

def logout_user(request):
    logout(request)
    context = RequestContext(request)
    return redirect('/login')

def add_room(request):
    context = RequestContext(request)
    habitacion=Habitacion()
    if request.method=='POST':
        hab=request.POST['habitacion']
        habitacion= Habitacion.objects.filter(id = habId)
        habitacion.nombre=hab
    return render_to_response('addroom.html',{'habitacion':habitacion},context)



def add_luces(request):
    context = RequestContext(request)
    if request.method=='POST':
        luces=request.POST['luces']
        luzId=request.POST['luzId']
        habId=request.POST['luzViene']
        luz=Luz()
        luz.nombre=luces
        luz.pin=luzId
        luz.lugar=habId
        luz.save
    luces = Luz.objects.filter(lugar_id = habId)
    habitacion= Habitacion.objects.filter(id = habId)
    return render_to_response('luz-agregada.html',{'luces':luces,'habitacion':habitacion},context)



def add_puertas(request):
    context = RequestContext(request)
    if request.method=='POST':
        puertas=request.POST['puertas']
        puertaId=request.POST['puertaId']
        habId=request.POST['puertaViene']
        puertas=Puerta()
        puerta.nombre=puerta
        puerta.pin=puertaId
        puerta.lugar=habId
        puerta.save
    puertas = Puerta.objects.filter(lugar_id = habId)
    habitacion= Habitacion.objects.filter(id = habId)
    return render_to_response('puerta-agregada.html',{'puertas':puertas,'habitacion':habitacion},context)


"""def mousemove_connection_factory(auth_class, pubsub):
    # Generate a new connection class using the default websocket connection
    # factory (we have to pass an auth class - provided by the server and a
    # pubsub singleton, also provided by the omnibusd server
    class GeneratedConnection(websocket_connection_factory(auth_class, pubsub)):
        def close_connection(self):
            # We subclassed the `close_connection` method to publish a
            # message. Afterwards, we call the parent's method.
            self.pubsub.publish(
                'mousemoves', 'disconnect',
                sender=self.authenticator.get_identifier()
            )
            return super(GeneratedConnection, self).close_connection()

    # Return the generated connection class
    return GeneratedConnection"""

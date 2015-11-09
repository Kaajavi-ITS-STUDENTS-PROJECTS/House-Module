from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import relay_functions
from module_1.models import Luz, Puerta, Habitacion, Sanitario, Alarma, Usuario, Regla
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
                    relay_functions.relay("close",puerta.pin)
                    puerta.status = False
                    print puerta.status
                else:
                    puerta.status = True
                    relay_functions.relay("open",puerta.pin)
                puerta.save()
                print puerta.status
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                if puerta.auto_close:
                    time.sleep(5)
                    relay_functions.relay("close",puerta.pin)
                    puerta.status = False
                    puerta.save()
    puertas = Puerta.objects.all()
    return render_to_response('puertas.html',{'puerta':puerta}, context)

def sanitario(request, id_sanitario):
    context = RequestContext(request)
    sanitario = Sanitario.objects.get(id = id_sanitario)
    if sanitario.ocupado:
        sanitario.ocupado = False
    else:
        sanitario.ocupado = True
    sanitario.save()
    return redirect('/')


def habitacion(request):
    context = RequestContext(request)
    id= request.POST.get('id')
    lista_permitidos = Usuario.objects.filter(permisos_habitaciones=id)
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                habitacion = Habitacion.objects.get(id = id)
                luces = Luz.objects.filter(lugar_id = id)
                for luz in luces:
                    if luz:
                        status_l = True
                    else:
                        status_l = False
                        break

                if habitacion.status and status_l:
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
                return redirect("/")
            else:
                return render_to_response('login.html',
                              context)
        else:
            return render_to_response('login.html',
                              context)
    else:
        return render_to_response('login.html',
                              context)

def logout_user(request):
    logout(request)
    context = RequestContext(request)
    return redirect('/login')

"""def add_room(request):
    context = RequestContext(request)
    if request.method=='POST':
        hab = request.POST['habitacion']
        habitacion = Habitacion()
        habitacion.nombre=hab
        habitacion.save()
    return render_to_response('addroom.html',context)



def add_luces(request):
    context = RequestContext(request)
    if request.method=='POST':
        print "adentro"
        luces=request.POST['luzNombre']
        luzId=request.POST['luzId']
        habId = Habitacion.objects.latest('id')
        luz=Luz()
        luz.nombre=luces
        luz.pin=luzId
        luz.lugar=habId
        luz.save()
    luces = Luz.objects.filter(lugar_id = habId.id)
    print "afuera", luces, " ", Luz.objects.all()
    return render_to_response('luz-agregada.html',{'luces':luces},context)

def add_puertas(request):
    context = RequestContext(request)
    if request.method=='POST':
        puerta=request.POST['puertaNombre']
        puertaId=request.POST['puertaId']
        habId = Habitacion.objects.latest('id')
        puertas=Puerta()
        puertas.nombre=puerta
        puertas.pin=puertaId
        puertas.lugar=habId
        if request.POST['autoPuerta'] == "false":
            puertas.auto_close=False
            print request.POST['autoPuerta']
        else:
            puertas.auto_close=True
            print "true"
        puertas.save()
    puertas = Puerta.objects.filter(lugar_id = habId.id)
    return render_to_response('puerta-agregada.html',{'puertas':puertas},context)"""


def auto_luz(request):
    context = RequestContext(request)
    luces = Luz.objects.all()
    rule = Regla.objects.all()

    return render_to_response('luzauto.html',{'luz':luces, 'rules':rule},context)

def add_rule(request):
    context = RequestContext(request)
    print "aca estoy"
    if request.method=='POST':
        print "hola"
        luz = Luz.objects.get(id = request.POST['id'])
        dias = eval(request.POST['days'])
        print dias,"-",request.POST['days']
        dias.pop(len(dias)-1)
        print "0"
        print dias,"-",request.POST['days']
        hora = eval(request.POST['hours'])
        print "1"
        regla = Regla()
        print "2"
        regla.relacion = luz
        print "3"
        regla.pin = luz.pin
        print "4"
        regla.status = request.POST['status']
        print "4"
        for i in dias:
            if i=="Lunes":
                print "Lun"
                regla.lun = True
            elif i=="Martes":
                print "Mar"
                regla.mar = True
            elif i=="Miercoles":
                print "Mie"
                regla.mie = True
            elif i=="Jueves":
                print "Jue"
                regla.jue = True
            elif i=="Viernes":
                print "Vie"
                regla.vie = True
            elif i=="Sabado":
                print "Sab"
                regla.sab = True
            elif i=="Domingo":
                print "Dom"
                regla.dom = True
        regla.from_hour = hora[0]
        print "from"
        regla.to_hour = hora[1]
        print "to"
        regla.save()
        print "save"
    rule = Regla.objects.all()
    return render_to_response('tab.html',{'rules':rule},context)

def del_rule(request):
    context = RequestContext(request)
    rule = Regla.objects.get(id = request.POST['id_r'])
    rule.delete()
    rules = Regla.objects.all()
    return render_to_response('tab.html',{'rules':rules},context)

def get_current_user(request):
    context = RequestContext(request)
    print request.user.username
    username = request.user
    if request.user.is_authenticated():
        return render_to_response('perfil.html',{'username':username},context)
    else:
        return render_to_response('perfil.html',{'username':""},context)


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

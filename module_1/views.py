from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import relay_functions
from module_1.models import Luz, Puerta, Habitacion, Sanitario, Alarma, Usuario, Regla, Log
from django.contrib.auth import authenticate
import time
from djcelery.models import PeriodicTask, CrontabSchedule
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


def recargar(helper, result):
    publish(
        'module_recargar',
        'reload',
        sender='server'  # sender id of the event, can be None.
    )

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
                    setLuz(False, luz)
                else:
                    luz.status=True
                    setLuz(True, luz)
                luz.save()
    luces = Luz.objects.all()
    return render_to_response('luces.html',{'luz':luz}, context)


def setLuz(status, luz ):
    log=Log()
    log.output=luz
    log.status=status
    if status==True:
        relay_functions.relay("open",luz.pin)
    else:
        relay_functions.relay("close",luz.pin)
    log.save()


def puerta(request):
    context = RequestContext(request)
    id= request.POST.get('id')
    puerta = Puerta.objects.get(id = id)
    lista_permitidos = Usuario.objects.filter(permisos_puertas=id)
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                if puerta.status:
                    setPuerta(False,puerta)
                    puerta.status = False
                    print puerta.status
                else:
                    puerta.status = True
                    setPuerta(True, puerta)
                puerta.save()
                print puerta.status
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                if puerta.auto_close:
                    print "helper"
                    helper = "#puerta-" + str(puerta.id)
                    print "recargar"
                    recargar(helper, render_to_response('puertas.html',{'puerta':puerta}, context))
                    print "time sleep"
                    time.sleep(5)
                    print "cerrar puerta"
                    setPuerta(False,puerta)
                    print "guarda status"
                    puerta.status = False
                    print "save"
                    puerta.save()
    print "Fuera del if"
    puertas = Puerta.objects.all()
    return render_to_response('puertas.html',{'puerta':puerta}, context)

def setPuerta(status, puerta ):
    log=Log()
    log.output=puerta
    log.status=status
    if status==True:
        relay_functions.relay("open",puerta.pin)
    else:
        relay_functions.relay("close",puerta.pin)
    log.save()

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
                        setLuz(False,luz)
                        luz.status = habitacion.status
                        luz.save()
                else:
                    habitacion.status = True
                    for luz in luces:
                        setLuz(True,luz)
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
    #periodic = PeriodicTask.objects.all()
    #cron = CrontabSchedule.objects.all()
    if request.method=='POST':
        print "hola"
        luz = Luz.objects.get(id = request.POST['id'])
        dias = eval(request.POST['days'])
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
        if request.POST['status'] == "false":
            regla.status=False
            print request.POST['status']
        else:
            regla.status=True
            print "true"
        print "4"
        days_t = []
        for i in dias:
            if i=="Lunes":
                print "Lun"
                regla.lun = True
                days_t.append(1)
            elif i=="Martes":
                print "Mar"
                regla.mar = True
                days_t.append(2)
            elif i=="Miercoles":
                print "Mie"
                regla.mie = True
                days_t.append(3)
            elif i=="Jueves":
                print "Jue"
                regla.jue = True
                days_t.append(4)
            elif i=="Viernes":
                print "Vie"
                regla.vie = True
                days_t.append(5)
            elif i=="Sabado":
                print "Sab"
                regla.sab = True
                days_t.append(6)
            elif i=="Domingo":
                print "Dom"
                regla.dom = True
                days_t.append(0)
        regla.from_hour = hora[0]
        f_h = str(hora[0])
        print "from"
        regla.to_hour = hora[1]
        t_h = str(hora[1])
        print "to"
        regla.save()
        print "save"
        cron = CrontabSchedule()
        cron.minute = f_h[-2:]
        cron.hour = f_h[:2]
        print days_t
        aux=""
        for i in range(len(days_t)):
            if i == len(days_t)-1:
                aux += str(days_t[i])
            else:
                aux += str(days_t[i])+","
        days_t = aux
        print days_t
        cron.day_of_week = days_t
        cron.save()
        print "cron save"
        regla = Regla.objects.latest('id')
        cronT = CrontabSchedule.objects.latest('id')
        print "regla y cronT"
        periodic = PeriodicTask()
        print "P_t"
        na = str(regla.id)+"_1"
        print "na"
        periodic.name = na
        print "name"
        if regla.status:
            periodic.task = "module_1.tasks.on"
        else:
            periodic.task = "module_1.tasks.off"
        print "status"
        periodic.crontab = cronT
        print "cron= p_t"
        periodic.args = "[ " +str(regla.pin)+ " ]"
        print "arg"
        periodic.save()
        print "periodic save"

        cron = CrontabSchedule()
        cron.minute = f_h[-2:]
        cron.hour = f_h[:2]
        print days_t
        aux=""
        for i in range(len(days_t)):
            if i == len(days_t)-1:
                aux += str(days_t[i])
            else:
                aux += str(days_t[i])+","
        days_t = aux
        print days_t
        cron.day_of_week = days_t
        cron.save()
        print "cron save"
        cronT = CrontabSchedule.objects.latest('id')
        print "regla y cronT"
        periodic = PeriodicTask()
        print "P_t"
        na = str(regla.id)+"_2"
        print "na"
        periodic.name = na
        print "name"
        if regla.status:
            periodic.task = "module_1.tasks.on"
        else:
            periodic.task = "module_1.tasks.off"
        print "status"
        periodic.crontab = cronT
        print "cron= p_t"
        periodic.args = "[ " +str(regla.pin)+ " ]"

        print "arg"
        periodic.save()
        print "periodic save"

    rule = Regla.objects.all()
    return render_to_response('tab.html',{'rules':rule},context)

def del_rule(request):
    context = RequestContext(request)
    rule = Regla.objects.get(id = request.POST['id_r'])
    na = str(rule.id)+"_1"
    periodic = PeriodicTask.objects.get(name = na)
    periodic.delete()
    na = str(rule.id)+"_2"
    periodic = PeriodicTask.objects.get(name = na)
    periodic.delete()
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

def logs(request):
    context = RequestContext(request)
    logs = Log.objects.all()
    logs = logs[::-1]
    fechas = []
    cont = 0
    for log in logs:
        if log.fecha!=fechas[cont]:
            fechas[cont]==log.fecha
        cont+=1

    return render_to_response('logs.html',{'logs':logs,'fechas':fechas},context)

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

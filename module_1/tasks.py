from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
import relay_functions
relay_functions.setting_pines()
@task
def on(pin):
    relay_functions.relay("open" ,pin)

#@task
#def off(pin):
#    relay_functions.relay("close" ,pin)

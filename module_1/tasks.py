from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
import relay_functions

logger = get_task_logger(__name__)
# A periodic task that will run every minute (the symbol "*" means every)

@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="1")))
def scraper_example():
    relay_functions.relay("open" ,15)


@task
def on():
    relay_functions.relay("open" ,15)

#@task
#def off(pin):
#    relay_functions.relay("close" ,pin)

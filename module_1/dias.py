from django.utils.translation import ugettext as _
from django.db.models import SmallIntegerField


DAY_OF_THE_WEEK = {
    '1' : _(u'Lunes'),
    '2' : _(u'Martes'),
    '3' : _(u'Miercoles'),
    '4' : _(u'Jueves'),
    '5' : _(u'Viernes'),
    '6' : _(u'Sabado'),
    '7' : _(u'Domingo'),
}

class dias(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1
        super(DayOfTheWeekField,self).__init__(*args, **kwargs)

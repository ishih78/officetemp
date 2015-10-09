from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Temperature

temp_f = 73

def index(request):
    temperature = Temperature(degrees=temp_f)
    room_condition = temperature.display_room_condition()
    template = loader.get_template('officetemp/index.html')
    context = RequestContext(request, {
        'room_condition': room_condition,
        'temp_f': temp_f,
    })
    return HttpResponse(template.render(context))

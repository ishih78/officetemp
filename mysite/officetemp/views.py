from django.http import HttpResponse
from django.template import RequestContext, loader

import os
import glob
import time
import subprocess

from .models import Temperature

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
        catdata = subprocess.Popen(['cat',device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = catdata.communicate()
        out_decode = out.decode('utf-8')
        lines = out_decode.split('\n')
        return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = round(temp_c * 9.0 / 5.0 + 32.0)
    return temp_f

def index(request):
    degrees_now = read_temp()
    temperature = Temperature(degrees=degrees_now)
    room_condition = temperature.display_room_condition()
    template = loader.get_template('officetemp/index.html')
    context = RequestContext(request, {
        'room_condition': room_condition,
        'temp_f': degrees_now,
    })
    return HttpResponse(template.render(context))

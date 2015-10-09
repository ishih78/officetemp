import os
import glob
import time
import json
# import hipchat
import requests
import urllib2


#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

# base_dir = '/sys/bus/w1/devices/'
# device_folder = glob.glob(base_dir + '28*')[0]
# device_file = device_folder + '/w1_slave'
# hipster = hipchat.HipChat(token="OpYNciUskcNLfyAQV9A2O49loJg444S6xAfEk560")

# def read_temp_raw():
#     f = open(device_file, 'r')
#     lines = f.readlines()
#     f.close()
#     return lines

def read_temp():
    # lines = read_temp_raw()
    # while lines[0].strip()[-3:] != 'YES':
    #     time.sleep(0.2)
    #     lines = read_temp_raw()
    # equals_pos = lines[1].find('t=')
    # if equals_pos != -1:
    #     temp_string = lines[1][equals_pos+2:]
        temp_c = 22.0
        temp_f = 72.0
        if temp_f > 70:
            condition = "hot"
        elif temp_f < 70:
            condition = "cold"
        else:
            condition = "comfy"

        temp_json = json.dumps({"degC": temp_c, "degF": temp_f, "condition": condition})
        # hipmsg = hipster.method('rooms/message', method='POST', parameters={'room_id': 2025691, 'from': 'Irene', 'message': temp_json})
        # room_info = {"room_id": 2025691, "from": "Irene", "message": temp_json}
        # mytoken = "OpYNciUskcNLfyAQV9A2O49loJg444S6xAfEk560"
        # url = "https://api.hipchat.com/v2/room/message?auth_token=" + mytoken
        # response = requests.post(url, params=room_info)

        return temp_json

while True:
        print(read_temp())
        time.sleep(1)

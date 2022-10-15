from win10toast import ToastNotifier
import requests
import json
import time


while True:    
    api_url = "http://www.boredapi.com/api/activity/"

    response = requests.get(api_url)
    content = response.content.decode("UTF-8")

    dict_content = json.loads(content)

    toaster = ToastNotifier()
    toaster.show_toast(dict_content["activity"], dict_content["link"], icon_path=None, duration=10, threaded=True)
    time.sleep(10)
    

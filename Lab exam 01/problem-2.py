import requests
import json
import time;
from win10toast import ToastNotifier
toaster = ToastNotifier()

api_url = "https://api.openweathermap.org/data/2.5/weather?q=chittagong&appid=4b5f5c378962441c1c0063e2bb400c5c";

response = requests.get(api_url)
content = response.content.decode("UTF-8")

dict_content = json.loads(content)

while True:
    main = dict_content['main'];
    temp = main['temp'];
    toaster.show_toast("Your 30 minute weather reminder ",
                   f"Today's temperature is {temp}",
                   icon_path=None,
                   duration=5,
                   threaded=True)
    time.sleep(1800)

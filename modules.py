# built-in modules -> pythona yüklü gelen (math,date)
# local modules -> projede bizim ürettiğimiz dosyalar (oop.py)
# paket yöneticisinde bulunan 3. taraf kütüphaneler (pip)

#
# import math # math kütüphanesini komple import et
from math import sqrt as karekok, cos # math kütüphanesinden sqrt fonk. import et
# alias -> takma ad
import oop
import requests

#print(math.sqrt(25))
print(karekok(25))
print(cos(90))

#car1 = oop.Car("Hyundai")
#car1.increase_speed(50)

response = requests.get("https://google.com")
print(response.status_code)
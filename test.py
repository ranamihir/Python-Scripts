import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

download_web_image('https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xap1/v/t1.0-9/s480x480/10858382_10202101044326456_7418781523648908301_n.jpg?oh=dc6b13675df534f15828607ab9df8a11&oe=54FA75DA&__gda__=1425775713_f75b9566c866dca6eb27ec27f3e6b3ed')
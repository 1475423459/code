#coding=utf-8
import requests
url='http://t.weather.sojson.com/api/weather/city/101030100'
r=requests.get(url)
print(r.text)
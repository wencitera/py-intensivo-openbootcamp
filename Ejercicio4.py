import requests
import json

def main():
    request_api()

def request_api():
    ciudad = 'i'
    while ciudad != '':
        ciudad = input('Ingrese una ciudad, aprentar enter para salir: \n')
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid=08a5a8b2ac581de38ad79470616dba38')
        datos = json.loads(r.text)
        print(f'Mínima: {kelvin_to_celsius(datos["main"]["temp_min"])} \nMáxima: {kelvin_to_celsius(datos["main"]["temp_max"])} ')

def kelvin_to_celsius(k):
    return k - 273.15

if __name__ == '__main__':
    main()
import requests
import datetime

now = datetime.datetime.now()

appid = "7357700e5a37a9c82f46d4d0d4981cca"

city = input("wybierz Polskie miasto\n")
print("\n" + "=" * 50 + "\n")
city += ",pl"

def weather(city):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
        params={'q': city, 'units': 'metric', 'lang': 'pl', 'APPID': appid})
        data = res.json()
        day_s = now.day
        for i in data['list']:
            if day_s + 1 == int(i['dt_txt'][8:10]):
                day_s += 1
                print("\n" + "=" * 50 + "\n")
            if int(i['dt_txt'][8:10]) - now.day > 3:break
            print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
    except Exception as e:
        print("miasto jest napisane niepoprawnie")
    pass

weather(city)

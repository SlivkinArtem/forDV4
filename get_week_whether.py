from pprint import pprint

import matplotlib.pyplot as plt

import datetime
#data[0] descr
import requests
def tempretures():
    appid = '8be2336bf0e5e7ed40d23b4bd3ef565a'

    request = requests.get('http://api.openweathermap.org/data/2.5/onecall',
                           params = {'lat' : '61.68', 'lon' : 50.81, 'APPID' : appid, 'units': 'metric', 'lang' : 'ru',
                                     'exclude' : 'current,minutely,hourly,alerts'})
    data = request.json()
    dates = []
    morning = []
    morning_feels = []
    #pprint(data)
    for day in data['daily']:
        dates.append(datetime.datetime.fromtimestamp(day['dt']).strftime('%d.%m'))
        morning.append(day['temp']['morn'])
        morning_feels.append(day['feels_like']['morn'])
        print(f"Дата : {datetime.datetime.utcfromtimestamp(day['dt']).strftime('%d.%m.%y')}")
        print(f"Температура утром : {day['temp']['morn']}. По ощущениям: {day['feels_like']['morn']}")
        print(f"Температура днем : {day['temp']['day']}. По ощущениям: {day['feels_like']['day']}")
        print(f"Температура вечером : {day['temp']['eve']}. По ощущениям: {day['feels_like']['eve']}\n")

    plt.figure(figsize=(16, 8))
    plt.subplot(2, 1, 1)
    plt.plot(dates, morning, c = 'red', lw=1.5, label='Температура')
    plt.plot(morning_feels, c='blue', lw=1.5, label='Температура по ощущениям')
    plt.title('Утро')
    plt.legend()
    plt.grid()


print(tempretures())


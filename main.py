import datetime
import time
import requests
from plyer import notification


NIVEL_GUAIBA_URL = 'https://nivelguaiba.com/all'


def get_water_level():
    req = requests.get(NIVEL_GUAIBA_URL)
    current_date = datetime.datetime.now().date().strftime("%d/%m/%Y")
    raw_data = str(req.content).split(current_date)
    current_water_level = raw_data[1].split('<td>')[1].split('</td>')[0]
    return current_water_level


def notifier_system():
    while True:
        water_level = get_water_level()

        notification.notify(
            title="Alerta dos guri!",
            message=f"Se cuida, o nível atual do Guaíba tá em: {water_level}",
            timeout=10
        )
        time.sleep(60*5)


if __name__ == "__main__":
    notifier_system()

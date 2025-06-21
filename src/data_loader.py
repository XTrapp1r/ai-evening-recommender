import requests

def get_weather(city_name: str, api_key: str) -> dict:
    """
    Получает текущую погоду по названию города.
    Возвращает словарь с температурой, описанием и др.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'температура': data['main']['temp'],
            'ощущается как': data['main']['feels_like'],
            'погодное описание': data['weather'][0]['description'],
            'ветер': data['wind']['speed']
        }
        return weather
    else:
        print("Ошибка при получении погоды:", response.status_code)
        return {}

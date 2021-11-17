from actions_toolkit import core

from app.weather import weather_bot

if __name__ == '__main__':
    push_url = core.get_input('webhook')
    city_code = core.get_input("city_code")
    weather_bot(city_code, push_url)

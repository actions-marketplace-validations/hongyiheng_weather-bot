from actions_toolkit import core

from app.weather import weather_bot, work_wx_push

if __name__ == '__main__':
    push_url = core.get_input('webhook')
    city_code = core.get_input("city_code")
    from_data = weather_bot(city_code)
    work_wx_push(from_data, push_url)

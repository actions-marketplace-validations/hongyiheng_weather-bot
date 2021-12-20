import requests


def weather_bot(city_code):
    api = 'http://t.weather.itboy.net/api/weather/city/'
    url = api + city_code
    response = requests.get(url)
    resp = response.json()
    if resp['status'] == 200:
        city = resp["cityInfo"]["city"]
        date = resp["data"]["forecast"][0]["ymd"]
        week = resp["data"]["forecast"][0]["week"]
        weather_type = resp["data"]["forecast"][0]["type"]
        temperature_high = resp["data"]["forecast"][0]["high"]
        temperature_low = resp["data"]["forecast"][0]["low"]
        humidity = resp["data"]["shidu"]
        pm25 = str(resp["data"]["pm25"])
        pm10 = str(resp["data"]["pm10"])
        quality = resp["data"]["quality"]
        fx = resp["data"]["forecast"][0]["fx"]
        fl = resp["data"]["forecast"][0]["fl"]

        push_content = "**[" + city + "] 天气**\n"
        push_content += "日期： " + date + " " + week + "\n"
        push_content += "天气： " + weather_type + "\n"
        push_content += "温度： " + temperature_low + " / " + temperature_high + "\n"
        push_content += "湿度： " + humidity + "\n"
        push_content += "空气： " + quality + " （PM2.5：" + pm25 + "， PM10：" + pm10 + "）\n"
        push_content += "风况： " + fx + fl
        form_data = {
            "msgtype": "markdown",
            "markdown": {
                "content": push_content
            }
        }
        return form_data


def work_wx_push(form_data, push_urls):
    headers = {"Content-Type": "text/plain"}
    urls = push_urls.split(",")
    for url in urls:
        res = requests.post(url=url, headers=headers, json=form_data)
        print(res.text)

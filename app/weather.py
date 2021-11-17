import requests


def weather_bot(city_code, push_urls):
    api = 'http://t.weather.itboy.net/api/weather/city/'
    url = api + city_code
    response = requests.get(url)
    resp = response.json()
    if resp['status'] == 200:
        city = resp["cityInfo"]["city"]
        date = resp["data"]["forecast"][0]["ymd"]
        week = resp["data"]["forecast"][0]["week"]
        weather_type = resp["data"]["forecast"][0]["type"]
        wendu_high = resp["data"]["forecast"][0]["high"]
        wendu_low = resp["data"]["forecast"][0]["low"]
        shidu = resp["data"]["shidu"]
        pm25 = str(resp["data"]["pm25"])
        pm10 = str(resp["data"]["pm10"])
        quality = resp["data"]["quality"]
        fx = resp["data"]["forecast"][0]["fx"]
        fl = resp["data"]["forecast"][0]["fl"]

        push_content = "**[" + city + "] 天气**\n"
        push_content += "日期： " + date + " " + week + "\n"
        push_content += "天气： " + weather_type + "\n"
        push_content += "温度： " + wendu_low + " / " + wendu_high + "\n"
        push_content += "湿度： " + shidu + "\n"
        push_content += "空气： " + quality + " （PM2.5：" + pm25 + "， PM10：" + pm10 + "）\n"
        push_content += "风况： " + fx + fl

        form_data = {
            "msgtype": "markdown",
            "markdown": {
                "content": push_content
            }
        }
        headers = {"Content-Type": "text/plain"}
        urls = push_urls.split(",")
        for url in urls:
            res = requests.post(url=url, headers=headers, json=form_data)
            print(res.text)

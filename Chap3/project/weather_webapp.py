#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import requests
import json

history_list = []

def city_weather(city):
    API = 'https://api.seniverse.com/v3/weather/now.json'
    params = {'key': '4r9bergjetiv1tsd', 'location': city, 'language': 'zh-Hans', 'unit': 'c'}
    res = requests.get(API, params = params)
    res.status_code == requests.codes.ok
    dic = json.loads(res.text)

    if 'status' in dic and dic['status_code'] == 'AP010010':
        message = '您输入的城市有误，或不在可查询范围内，请您重新输入。'
    elif 'results' in dic:
        results_list = dic['results']
        weather_now = results_list[0]['now']
        weather = weather_now['text']
        temperature = weather_now['temperature']
        wind = weather_now['wind_direction']
        time = results_list[0]['last_update']
        update_time = time[:10] + ' ' + time[11:16]

        message = f'{city}的天气为{weather}，风向为{wind}风，温度为{temperature}摄氏度。\n更新时间：{update_time}'

        if message not in history_list:
            history_list.append(message)

    return message



app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/user', methods=['GET','POST'])
def result():
    city = request.args.get('city')
    query = request.args.get("query")
    history = request.args.get("history")
    h = request.args.get("help")

    if query == "查询":
        if city:
            message = city_weather(city)
            result = [message]
        else:
            message = "请输入您想要查询的城市"
            result = [message]

    if history == "历史":
        if history_list == []:
            message = "您还没有查询过任何城市的天气。"
            result = [message]
        else:
            message = '您查询过的城市及其天气为：'
            for one_city in history_list:
                result = [message] + history_list
    if h == "帮助":
        result = ["使用提示：", "1. 输入城市名，查询该城市的天气；",
        "2. 输入help，获取使用提示；", "3. 输入history，获取查询历史；",
        "4. 输入quit，退出天气查询程序。"]


    return render_template("home.html", result=result)


if __name__ == '__main__':
    app.run(debug = True)

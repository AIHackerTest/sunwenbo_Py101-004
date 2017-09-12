import requests
import json

history_list = []
finish = True


def quit():
    print('感谢您使用“天气通”。', end = '')
    print_history()
    print('欢迎下次使用，再见！\n')


def print_guide():
    print("使用提示：")
    print("    1. 输入城市名，查询该城市的天气；")
    print("    2. 输入help，获取使用提示；")
    print("    3. 输入history，获取查询历史；")
    print("    4. 输入quit，退出天气查询程序。")


def print_history():
    if history_list == []:
        print("您还没有查询过任何城市的天气。")
    else:
        print('您查询过的城市及其天气为：')
        for one_city in history_list:
            print(one_city)


def weather_check(city):
    API = 'https://api.seniverse.com/v3/weather/now.json'
    params = {'key': '4r9bergjetiv1tsd', 'location': city, 'language': 'zh-Hans', 'unit': 'c'}
    res = requests.get(API, params = params)
    res.status_code == requests.codes.ok

    dic = json.loads(res.text)
    if 'status' in dic and dic['status_code'] == 'AP010010':
        print('您输入的指令有误，或不在可查询范围内，请您重新输入。')
    elif 'results' in dic:
        results_list = dic['results']
        weather_now = results_list[0]['now']
        weather = weather_now['text']
        temperature = weather_now['temperature']
        wind = weather_now['wind_direction']
        time = results_list[0]['last_update']
        update_time = time[:10] + ' ' + time[11:16]

        weather_report = f'{city}的天气为{weather}，风向为{wind}风，温度为{temperature}摄氏度。\n更新时间：{update_time}'
        print(weather_report)

        if weather_report not in history_list:
            history_list.append(weather_report)
    else:
        print('程序正在维护中，暂无法提供服务，抱歉给您带来不便。')
        exit(0)


print_guide()

while finish:
    from_user = input('\n请输入您的指令或想要查询的城市：')
    if from_user == 'quit':
        quit()
        finish = False
    elif from_user == 'help':
        print_guide()
    elif from_user == 'history':
        print_history()
    elif from_user == '':
        pass
    else:
        weather_check(from_user)

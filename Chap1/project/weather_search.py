# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv


# prepare weather_dict and city_list
with open(filename, 'r', encoding='UTF-8') as f:
    data = f.readlines()

weather_dict = {}
for line in data:
    key, value = line.strip().split(',')
    weather_dict[key] = value

city_list = list(weather_dict.keys())


# define functions
def print_guide():
    print("使用提示：")
    print("    1. 输入城市名，查询该城市的天气；")
    print("    2. 输入help，获取使用提示；")
    print("    3. 输入history，获取查询历史；")
    print("    4. 输入quit，退出天气查询程序。")
    user_input()

def weather_forecast(city):
    print(f'{city}的天气状况为：{weather_dict[city]}')
    history_record(city)
    user_input()

weather_history = []
def history_record(city):
    one_city = f'{city}：{weather_dict[city]}'
    if one_city not in weather_history:
        weather_history.append(one_city)

def print_history():
    if weather_history == []:
        print("您还没有查询过任何城市的天气。")
        print_guide()
    else:
        print('您查询过的城市及其天气为：')
        for one_city in weather_history:
            print(one_city)
        user_input()

def quit():
    print('感谢您使用“天气通”。', end = '')
    if weather_history == []:
        print("您还没有查询过任何城市的天气。")
    else:
        print('\n您查询过的城市及其天气为：')
        for one_city in weather_history:
            print(one_city)
    print('欢迎下次使用，再见！\n')
    exit()

def user_input():
    from_user = input('\n请输入您的指令或想要查询的城市：')
    if from_user == 'help':
        print_guide()
    elif from_user == 'quit':
        quit()
    elif from_user == 'history':
        if weather_history == []:
            print("您还没有查询过任何城市的天气。")
            user_input()
        else:
            print_history()
    elif from_user in city_list:
        weather_forecast(from_user)
    else:
        similar_city = ''
        for city in city_list:
            if from_user.find(city) != -1:
                similar_city = similar_city + city
                break
        if len(similar_city) != 0:
            print(f'您输入的城市名未被识别，您可以尝试输入更简洁的城市名：{similar_city}')
            user_input()
        else:
            print("您的输入有误，或不在可查询范围内，请重新输入。")
            user_input()

            
print('\n欢迎使用“天气通”，您可以使用“天气通”查询所有中国城市的天气。请您阅读下面的使用提示。')
print_guide()
user_input()

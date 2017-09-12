i = 1

def user_input(i):
	city = 'hangzhou'
	print_use(i, city)

def print_use(i, city):
    print(i, city)
    i = i + 1
    if i < 500:
        user_input(i)

user_input(i)

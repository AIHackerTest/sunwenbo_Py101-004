import random

correct_number = random.randint(0, 20)

print("欢迎您参加猜数字游戏，程序会随机生成一个不小于0且不大于20的整数，您有10次机会猜测这个整数是多少。", end = "")
print("您每猜测一个数字，程序都会给您反馈，告诉您猜准了、猜大了或猜小了。现在游戏正式开始。")

for i in range(0, 10):
    def guess_a_number():
        try:
            guess_number = int(input("\n现在请您进行第{}次猜测，请输入您猜测的数字：".format(i + 1)))
            return guess_number
        except ValueError:
            print("\n您输入的不是整数，需要重新输入。")
            return guess_a_number()

    guess_number = guess_a_number()

    if guess_number == correct_number:
        print("恭喜您，您猜对了!现在游戏结束，再见！\n")
        break
    elif guess_number > correct_number:
        if i < 9:
            print("对不起，您猜测的数字偏大。接下来您还有{}次猜测机会".format(9 - i))
        else:
            print("对不起，您猜测的数字偏大。您已经用完了所有机会，现在游戏结束，再见。")
            break
    else:
        if i < 9:
            print("对不起，您猜测的数字偏小。接下来您还有{}次猜测机会".format(9 - i))
        else:
            print("对不起，您猜测的数字偏小。您已经用完了所有机会，现在游戏结束，再见。")
            break

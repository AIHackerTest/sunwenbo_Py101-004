import random

# 用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
def correct_number():
    number_list = random.sample(range(0, 9), 4)
    while number_list[0] == 0:
        number_list = random.sample(range(0, 9), 4)

    new_number_list = [str(n) for n in number_list]

    return new_number_list

correct_list = correct_number() # 正确答案以列表形式储存

# 说明游戏规则
print("欢迎您参加猜数字游戏，程序会随机生成一个4位数的整数，每个数位上的数字不重复，且首位数字不为零，如1942。", end = "")
print("您有10次机会猜测这个整数是多少。")
print("您每猜测一个数字，程序都会给您反馈。反馈规则为：用A表示数字和位置都正确，用B表示数字正确但位置错误；用", end = "")
print("户猜测后，程序返回A和B的数量，例如2A1B表示用户所猜数字中，有2个数字的数字、位置都正确，有1个数字的数字", end = "")
print("正确但位置错误。")
print("现在游戏开始！")


# 玩家猜测数字
for i in range(0, 10):
    # 提醒玩家输入猜测的数字，若数字不符合规范，则要求玩家重新输入
    def guess_a_number():
        guess = input("\n现在请您进行第{}次猜测，请输入您猜测的数字：".format(i + 1))

        guess_list = [n for n in guess] # 将输入的文本转换为列表
        same = len(guess_list) == len(set(guess_list)) # 判断玩家输入的整数的不同数位是否有相同数字

        bool = (guess.isdigit()) and (len(guess) == 4) and (guess[0] != "0") and same

        if bool:
            return guess_list
        else:
            print("您的输入不符合要求。请输入一个4位数的整数，每个数位上的数字不重复，且首位数字不为零。")
            return guess_a_number()

    guess_list = guess_a_number()

    # 计算A和B的个数
    count_A = 0
    count_B = 0
    for j in range(0, 4):
        if guess_list[j] == correct_list[j]:
            count_A = count_A + 1
        else:
            if guess_list[j] in correct_list:
                count_B = count_B + 1

    # 反馈猜测结果
    if count_A == 4:
        print("恭喜您，您猜对了!您一共使用了{}次机会。现在游戏结束，再见！\n".format(i + 1))
        exit(0)
    else:
        if i < 9:
            print("您还未猜到正确的数字。提示：{}A{}B。\n您还有{}次猜测的机会".format(count_A, count_B, 9 - i))
        else:
            answer = ''.join(correct_list)
            print(f"对不起，您已经用完了10次机会，正确的答案是{answer}。现在游戏结束，再见。")
            exit(0)

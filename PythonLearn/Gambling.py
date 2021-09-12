# -*- coding : UTF-8 -*-
# @Time : 2021/8/7 23:08
# @Author : Hierarch
# @File : Gambling.py
# @Software : PyCharm

"""
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
初始金2000,玩家可自行下注
"""

import random
# from random import randint


player_money = 2000  # 玩家的初始金
while player_money > 0:  # 当玩家有钱的时候才能进行赌
    print(f'您的本金还有：{player_money}')
    player_bet = int(input('请下注（请输入正整数）：'))
    if player_bet > player_money or player_bet <= 0:
        print('扯犊子')
    else:
        player = random.randint(1, 6) + random.randint(1, 6)  # 随机生成两个骰子随机数
        times = 1  # 第一次摇骰子
        print(f'您第{times}次摇骰子的点数是：{player}')
        if player == 7 or player == 11:
            player_money += player_bet
            print('您胜了！')
        elif player == 2 or player == 3 or player == 12:
            player_money -= player_bet
            print('庄家胜！')
        else:
            while True:
                times += 1
                player_2 = random.randint(1, 6) + random.randint(1, 6)
                print(f'您第{times}次摇骰子的点数是：{player_2}')
                if player_2 == 7:
                    player_money -= player_bet
                    print('庄家胜！')
                    break
                elif player_2 == player:
                    player_money += player_bet
                    print('您胜了！')
                    break
                else:
                    continue
else:
    print('穷鬼，你的钱已经输光了！')

"""
大佬的程序
"""

# money = 2000
# while money > 0:
#     print(f'你的总资产为: {money}元')
#     go_on = False
#     # 下注金额必须大于0小于等于玩家总资产
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     # 第一次摇色子
#     # 用1到6均匀分布的随机数模拟摇色子得到的点数
#     first = randint(1, 6) + randint(1, 6)
#     print(f'\n玩家摇出了{first}点')
#     if first == 7 or first == 11:
#         print('玩家胜!\n')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!\n')
#         money -= debt
#     else:
#         go_on = True
#     # 第一次摇色子没有分出胜负游戏继续
#     while go_on:
#         go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print(f'玩家摇出了{current}点')
#         if current == 7:
#             print('庄家胜!\n')
#             money -= debt
#         elif current == first:
#             print('玩家胜!\n')
#             money += debt
#         else:
#             go_on = True
# print('你破产了, 游戏结束!')

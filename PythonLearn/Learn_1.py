# -*- coding : UTF-8 -*-
# @Time :  20:04
# @Author : Hierarch
# @File : Learn_1.py
# @Software : PyCharm

# print('hello world')
# num_1 = 10
# print(type(num_1))
# num_2 = 4
# print(type(num_2))
# num_3 = num_1 / num_2
# print(type(num_3))
#
# num_comp = complex(5, 2)
# print(num_comp)
#
# info = '''
#             123321
#             321321
#         '''
# print(info)
# input_data = input('Please input something:')
# print(type(input_data))
# print('INFO is :', input_data)
#
# num_1 = float(input('The first num:'))
# num_2 = float(input('The second num:'))
# num_3 = num_1 + num_2
# # print('%5.2f + %6.3f = %7.4f' % (num_1, num_2, num_3))
# print('%(num_1).3f + %(num_2).3f = %(num_3).3f' % vars())
# answer = input()
# j = 5
# for i in answer:
#     print(chr(ord(i) - j), end='')
#     j += 1
#
# num_1 = 3
# num_2 = 4 - 1
# num_3 = 2 + 1
# print('地址：%d' % id(num_1))
# print('地址：%d' % id(num_2))
#
# num_4 = 12
# num_5 = 12.0
# print('int address : %d, float address : %d, compare : %s,%s' % (id(num_4), id(num_5), (num_4 == nu
# m_5), (num_4 is num_5)))
# num_4 = 12
# num_5 = 12.0
# print('int address : %d, float address : %d, compare : %s,%s' % (id(num_4), id(num_5), (num_4 == num_5),
#                                                                  (num_4 is num_5)))

# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，
# 庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。

# num = 1
# total = 0
# while num <= 100:
#     total += num
#     num += 1
#     print(total)
# print(f'Total : {total}')
#
# # 斐波那契数列
# num_a = 0
# num_b = 1
# while num_b < 1000:
#     print(num_b, end=', ')
#     num_a, num_b = num_b, num_a + num_b
#
# # range 前闭后开
#
# str = 'HIERARCH.G.E.R.'
# for ger in str:
#     if 65 <= ord(ger) <= 90:
#         nb = ord(ger) + 32
#         print(chr(nb), end='')
#     else:
#         print(ger, end='')
#
# for x in range(1, 10):  # 控制行数
#     for y in range(1, x + 1):  # 当打印第一行第一个数字时，控制第二个数字的循环
#         print(f'{x} x {y} = {x * y}', end='\t')  # 打印公式
#     print()  # 换行
#
# line = 10  # 输出的总行数
# for a in range(0, line):  # 控制输出行数
#     for b in range(0, line - a):  # 随着行数的增加，空格随之减少
#         print('', end=' ')  # 打印空格
#     for c in range(0, a + 1):  # 随着行数的增加，* 随之增加
#         print('*', end=' ')  # 打印 *
#     print()  # 打印一行结束后换行

# line = 10  # 行数
# for x in range(0, line):  # 循环控制打印的行数
#     print(' ' * (line - x), end=' ')  # 打印空格的个数
#     print('* ' * (x + 1), end=' ')  # 打印*的个数 *后加空格
#     print()  # 换行

"""
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，例如：1**3 + 5**3 + 3**3 = 153。
"""
# for x in range(100, 999):
#     num_1 = (x % 10) ** 3  # 取个位数
#     num_2x = x % 100
#     num_2 = (num_2x // 10) ** 3  # 除以100的模取十位和个位，整除以10取十位的数字
#     num_3 = (x // 100) ** 3  # 取百位数字
#     sum = num_1 + num_2 + num_3
#     if sum == x:
#         print(x)
"""
将12345变成54321
"""
# x = 12345
# num_1 = x % 10  # 求个位数
# num_2 = x % 100 // 10  # 求十位数
# num_3 = x % 1000 // 100  # 求百位数
# num_4 = x % 10000 // 1000  # 求千位数
# num_5 = x // 10000  # 求万位数
# sum = num_1 * 10000 + num_2 * 1000 + num_3 * 100 + num_4 * 10 + num_5
# print(sum)

"""
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
# for male in range(0, 20):
#     for female in range(0, 34):
#         little = 100 - male - female
#         if little % 3 == 0 and male * 5 + female * 3 + little // 3 == 100:
#             print(f'{male}只公鸡，{female}只母鸡，{little}只小鸡')
#
# # 假设公鸡的数量为x，x的取值范围是0到20
# for x in range(0, 21):
#     # 假设母鸡的数量为y，y的取值范围是0到33
#     for y in range(0, 34):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

"""
打印素数
"""
# for x in range(2, 100):
#     is_prime = True
#     for y in range(2, x):
#         if x % y == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(x)

"""
计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""
# import random
# pc = random.randint(1, 101)
# times = 0
# while True:
#     times += 1
#     player = int(input('please input your answer:'))
#     if player < pc:
#         print('Bigger!')
#     elif player > pc:
#         print('Smaller!')
#     else:
#         print('Congratulations!')
#         break
# print(f'You\'v tried {times}times.')
"""
请输入一个数，判断是否是素数
"""
# num = int(input('Please input a number:'))
# is_prime = True
# for x in range(2, num):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print(f'{num} is prime')
# else:
#     print(f'{num} is\'t prime')
"""
列表
"""
# infos = [1, 2, 'shit', 'bro', 'wtf']
# print(infos[2])
# print(len(infos))
# print(infos[-3])
# print(infos)
# for x in range(5):
#     print(x)
# infos = infos + ['伞兵', 'motherfucker']
# print(infos)
# infos *= 3
# print(infos)
# print(len(infos))
# print(infos[17])
# print(infos)
# infos *= 3
# print(infos)
# infos2 = infos[0: 5]
# print(infos2)

info = ['shit', 'bro', 'damn it', 'wtf', 'up yours']
print(info)
info += ['fucker', 'MF', '肖战']
print(info)
print(len(info))
print(len(info[5]))
print(info[-3])
info2 = info[0: 5: 2]
print(info2)
for x in info:
    print(x)
info.remove('up yours')
print(info)
del info[1]
print(info)
infos = ['fuck', 'MF', '肖战', '吴亦凡', '罗志祥', 'damn it', 'wtf']
print(infos.pop(3))
print(infos)

# 模拟斗地主发牌，一共54张牌，黑桃('\u2660')，
# 梅花('\u2663')，方块('\u2665')，红桃('\u2666')，
# 大小王，A234...JQK
# 三个人玩，每人17张牌，底牌留三张
# 操作：
#     输入回车:打印第一个人的17张牌
#     输入回车:打印第二个人的17张牌
#     输入回车:打印第三个人的17张牌
#     输入回车:打印三张底牌
def get_cards():
    colors = ['\u2660', '\u2663', '\u2665', '\u2666']
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'J', 'Q', 'K']
    kings = ['大王', '小王']
    all = []
    for i in colors:
        for j in cards:
            card = i + ' ' + j
            all.append(card)
    allcards = all + kings
    return allcards

def myprint(l):
    for i in l:
        print(i, end = ' ')
    print()


import random as r
def poke_game():
    allcards = r.shuffle(get_cards())
    print(allcards)
    first = allcards[0,17]
    second = allcards[17,34]
    third = allcards[34,51]
    last = allcards[51,55]
    n = input('第一个人的牌是：')
    if n == '':
        myprint(first)    
    n = input('第二个人的牌是：')
    if n == '':
        myprint(second)
    n = input('第三个人的牌是：')
    if n == '':
        myprint(third)
    n = input('底牌是：')
    if n == '':
        myprint(last)

poke_game()
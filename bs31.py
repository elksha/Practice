from random import randrange

picked_list = []
whos_first = randrange(0, 2)


def computer_pick():
    computer_pick = randrange(1, 4)
    if (picked_list):
        if (picked_list[-1] + computer_pick >= 31):
            picked_list.append(31)
        else:
            picked_list.append(picked_list[-1] + computer_pick)
    else:
        picked_list.append(computer_pick)
    print('컴퓨터가 마지막에 부른 수 : %d' % (picked_list[-1]))


def player_pick():
    if (picked_list):
        number = 0
        player_pick = randrange(1, 4)
        if (((picked_list[-1] + 1) + 2) % 4 == 0):
            number = picked_list[-1] + 1
        elif (((picked_list[-1] + 2) + 2) % 4 == 0):
            number = picked_list[-1] + 2
        elif (((picked_list[-1] + 3) + 2) % 4 == 0):
            number = picked_list[-1] + 3
        else:
            number = picked_list[-1] + player_pick
        picked_list.append(number)
    else:
        player_pick = 2
        picked_list.append(player_pick)
    print('플레이어가 마지막에 부른 수 : %d' % (picked_list[-1]))


while(True):
    if (whos_first == 0):
        player_pick()
        computer_pick()
        if (picked_list[-1] == 31):
            print("플레이어 승리!")
            break
    elif (whos_first == 1):
        computer_pick()
        if (picked_list[-1] == 31):
            print("플레이어 승리!")
            break
        player_pick()

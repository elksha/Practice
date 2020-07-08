from time import sleep
import random
num = 0


def com():
    global num
    while True:
        i = random.randrange(1, 4)
        if num + i < 31:
            break
    for j in range(1, i + 1):
        num += 1
    print("컴퓨터가 %d를 불렀습니다!" % num)
    return


def user():
    global num
    while True:
        i = random.randrange(1, 4)
        if num + i in [2, 6, 10, 14, 18, 22, 26, 30]:
            break
    for j in range(1, i + 1):
        num += 1
    print("인공지능 유저가 %d를 불렀습니다!" % num)
    return


if __name__ == "__main__":
    turn = random.randrange(0, 2)

while num < 31:
    if turn == 0:
        com()
        turn = 1
    else:
        user()
        turn = 0
    sleep(1)

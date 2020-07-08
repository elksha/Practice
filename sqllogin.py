import sqlite3
from time import sleep


def logincheck():
    try:
        login = int(input("로그인을 하시려면 0, 회원가입을 하시려면 1을 입력해주세요 : "))
        print(login)
        return login
    except:
        print("올바르지 않은 입력입니다!")
        login = logincheck()
        return login


def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw


def signin(id, pw, cursor):
    user_check = 0
    for i in cursor.execute('SELECT id, pw FROM user'):
        if i[0] == id and i[1] == pw:
            user_check = 1
            print("로그인 성공!")
            break
    if (user_check == 0):
        print("로그인 실패...")


def existcheck(cursor):
    while(True):
        id, pw = user_input()
        exist_check = 0
        for i in cursor.execute('SELECT id, pw FROM user'):
            if i[0] == id:
                exist_check = 1
                print("이미 존재하는 아이디입니다!")
                sleep(1)
                break
        if exist_check == 1:
            continue
        else:
            return id, pw


def signup(id, pw, cursor):
    cursor.execute('insert into user values ("%s", "%s")' % (id, pw))
    print("%s님 회원가입 되었습니다!" % id)
    sleep(1)


def userlist(cursor):
    print("현재 존재하는 유저는")
    for i in cursor.execute('SELECT id, pw FROM user'):
        print("id: %s, pw: %s" % (i[0], i[1]))
    sleep(1)


def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    if stop == 1:
        exit()


def start():
    print("\n신나는 로그인/회원가입!!!!!")

    login = logincheck()

    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('create table if not exists user(id text, pw text)')
    conn.commit()

    if login == 0:
        id, pw = user_input()
        signin(id, pw, cursor)
    elif login == 1:
        id, pw = existcheck(cursor)
        signup(id, pw, cursor)
        conn.commit()
        userlist(cursor)
    else:
        print("올바른 숫자를 입력하세요!")

    conn.close()
    exitcheck()


start()

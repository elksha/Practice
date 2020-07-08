import csv

while True:
    name = input("이름을 입력해주세요: ")
    YMD = input("생년월일을 입력해주세요: ")
    id = input("아이디를 입력해주세요: ")
    password = input("비밀번호를 입력해주세요: ")
    # ??? 최소 1개 이상 쓰도록

    # 중복되는 id가 있는지
    with open('a.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        print(111)
        for i in csvreader:  # 수정 필요! 작동 x
            print(222)
            if (id == i[2]):
                print("이미 있는 아이디입니다. 다시 입력해주세요. \n")
            else:
                print(333)
                break

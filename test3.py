import csv

confirm = input('기존 회원이십니까?(Y/N): ')
if confirm == 'Y':
    print('로그인 페이지로 이동합니다.')
else:
    print('회원가입을 위한 정보 입력입니다. 아래의 정보를 입력해주세요.')
    with open('a.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([input('이름을 입력해주세요: '), input(
            'ID를 입력해주세요: '), input('비밀번호를 입력해주세요: ')])

with open('a.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for i in csvreader:
        print(i)
        if i[1] == input('ID: ') and i[2] == input('비밀번호: '):
            print('로그인되었습니다.')
        else:
            print('입력하신 정보를 확인해주세요.')

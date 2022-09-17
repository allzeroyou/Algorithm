sunsys = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

n = input()
if n.isnumeric():
    n = int(n)  # convert to integer
    if n >= 1:
        if n <= 8:  # 태양계 행성에 속함
            print(sunsys[n - 1])
        else:
            print('태양계는 8개 행성 뿐')
    elif n == 0:
        print('1~8사이값 입력')

elif int(n)<0:
    print(sunsys[int(n)])

else:
    print('숫자 입력')

# print('-2'.isnumeric()) # False 을 이용해서 예외처리 해보자

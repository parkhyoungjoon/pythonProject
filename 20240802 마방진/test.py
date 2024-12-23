# 수입력받기            isnumeric               1. 입력받고 홀수 확인 하는 함수
# 홀수인지 체크         조건문 if
# 짝수면 오류 프린트    %2 == 0 !=1
# 반복                  반복문 while

# 배열만들기                                    2. 입력받은 홀수로 배열 만들기 2차원배열 -> 값 0
# 배열수 = 입력받은수 * 입력받은수
# x, y축 시작값
# x = 입력받은수 // 2 절반
# y = 0 시작

# 조건                                          3. 반복할때만 x는 1씩 늘고 y는 1씩 줄어든다
# x = x+1
# y = y-1

# 조건                                          4. x는 입력받은수-1 보다 커지면 0이되어야 하고
# x = 입력받은수-1 < x ==> 0                       y는 0보다 작아지면 입력받은수-1이 되어야한다
# y = y < 0 ==> 입력받은수-1

# 조건
# x축 y축 배열안의 데이터가 이미 있을경우 0이 아닐경우 ==> y + 1            x,y축 배열안의 데이터가 0이 아니라면 y를 1더해준다 

# 반복

# 배열을 결과로 출력해주는 함수 1개
# 반복
   
# 모든 함수는 값을 리턴해줄때 반복중이든 조건 중이든 어떤경우에도 종료됨

# 함수 ==> 함수를 통해 값을 리턴해주는것 

def num_chk():
    while True:
        num = input('숫자 입력 ㄱㄱ씽')
        if num.isnumeric():
            num = int(num)
            if num%2 == 0:
                print('짝수 안대영')
                continue
            return num
        
def game_print(cube):
    for row in cube:
        for col in row:
            print(col,end=' ')
        print()

def game_start():
    input_data = num_chk()
    cube = [[0 for col in range(input_data)] for row in range(input_data)]
    x2 = input_data // 2
    y2 = 0
    i = 1

    while True:
        if i > input_data ** 2 : break
        # x = x+1 if x <= input_data-1 else 0       조건
        # y = y-1 if y >= 0 else input_data-1
        if cube[y2][x2] !=0:
            y2 = (y+1) % input_data              
            x2 = x
            continue
        x,y = x2, y2
        cube[y][x] = i

        x2 = (x+1) % input_data                     # 계산
        y2 = (y-1) % input_data
        i += 1
    game_print(cube)



game_start()
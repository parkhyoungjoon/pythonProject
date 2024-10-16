def sol_num_chk():              # 입력받은 문자열 이쁘게 만드는 함수
    while True:
        num = input('홀수차 배열의 크기를 입력하세요: ')
        if num.수():     # 숫자인지 체크
            num = int(num)      # 형변환 int
            if num % 2 == 1:    # 홀수 인지 체크
                return num
            else:
                print('짝수를 입력하였습니다. 다시 입력하세요')
        else:
            print('문자를 입력하였습니다. 다시 입력하세요')

def print_result(lists, cube_gob):
    num_area = len(str(cube_gob))   # 최대값의 자리수 구하기
    for row in lists:       
        for d in row:
            print(format(d, f'{num_area}'),end=' ')     # 최대값 자리수 만큼 포매팅
        print()

def game_start():
    cube_row_count = sol_num_chk()  # 홀수 입력받기
    cube = [[0 for col in range(cube_row_count)] for row in range(cube_row_count)] # 배열생성
    cube_limit = cube_row_count*cube_row_count # 배열의 총 길이 구하기
    x2 = cube_row_count // 2 # 열수 / 2 로 x2값 지정
    y2 = 0
    num = 1
    while True :
        if num > cube_limit : break
        if cube[y2][x2] != 0:       # 이미 값이 있는지 체크수
            y2 = (y+1) % cube_row_count
            x2 = x
            continue
        x, y = x2, y2
        cube[y][x] = num
        num += 1
        y2 = (y-1) % cube_row_count # 음수 나머지로 최대값 지정
        x2 = (x+1) % cube_row_count # 양수 나머지로 최대값 지정

    print_result(cube, cube_limit)

game_start()
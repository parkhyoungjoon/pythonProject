# -------- 공용변수 선언 -----------------------------------------------------------------------------------
import random

player = [{          # 플레이어 리스트 {내부 딕셔너리} 선언
    'name':'player', # 플레이어 이름
    'hp':4,          # hp 체력
    'dmg':1,         # dmg 데미지
    'item':[],       # item 아이템리스트
    'stat':0,
    'mind':0         # stat,mind 상태 아이템용 0 : 정상, 1 : 오함마 대기중, 최면상태
    },
    {
    'name':'dealer',
    'hp':4,
    'dmg':1,
    'item':[],
    'stat':0,
    'mind':0,
    'brain':0,
    'isView':True
    }]
itemName=['맥주','담배','돋보기','총기손질','최면','오함마'] # 아이템 이름 리스트
itemFirst = [4,5,1,2,0,3]
playMent = [
    [
        '스스로에게 총구를 겨눴다',
        '내 총끝이 딜러를 향한다',
        '꿀꺽...꿀꺽... 총알을 장전한다.',
        '쓰읍.... 후..... 매캐한 연기가 안쪽으로 들어온다. hp+1',
        '약실을 확인해본다...',
        '총기를 손질한다 다음번은 강하게 나갈것 같다 dmg+1',
        '쾅 제대로 걸렸다. 딜러의 팔을 내리쳤다'

    ],
    [
        '딜러가 스스로를 겨눴다.',
        '딜러의 총끝이 당신을 향한다',
        '벌컥벌컥, 으음 시원한데?',
        '"쓰읍~~ 하! 더 강한 건 없나?" hp+1',
        '좋아 어디 한번 볼까?',
        '아주 좋아 최고의 한방이야! dmg+1',
        '쾅!! 어디서 장난질이야!',
        '어떻게 해볼까?',
        '이렇게 하면 재미있겠는데!',
        '으음? 오랜만에 재밌는 상대로군!',
        '흐음 꽤나 강한걸?',
        '이거밖에 안되면 실망인데...',
        '아주 쉬워 쉽다구!'
        
    ]]
itemInfo = [
    '약실에 총알을 하나 제거합니다. *실탄이 제거 될수도 있습니다',
    '체력을 +1 올려줍니다',
    '약실에 총알이 있는지 없는지 확인합니다.',
    '총알의 데미지를 올립니다+1',
    '다음턴 상대방의 사격대상이 반대로 지정됩니다.',
    '다음턴 상대방이 아이템을 사용한다면 파괴하고 턴을 종료시킵니다'
    ]
turn = 0     # 턴 계산용 변수 ==> 0: 플레이어, 1: 딜러(컴퓨터)
bugshot = [] # 총리스트 선언 약실 전부 빈값(False)

# -------- Y / N 질문 체크 메서드 -------------------------------------------------------------------------
def yesOrNo(msg):
    while True:
        req = input(f'{msg} [입력해주세요] ( Y or N ) :') # 질문 받기
        if(req == 'Y' or req == 'y') :                   # Y or y일 경우 True반환
            return True
        elif(req == 'N' or req == 'n'):                  # N or n일 경우 False반환
            return False
        else:                                            # 둘다 아닐경우 다시 입력받음
            print('Y or N 둘중 하나만 입력해주세요')       # 경고문 출력
            continue

# -------- 벅샷 세팅 메서드 -------------------------------------------------------------------------------
def bugshotSetting():
    print("-철컥 !..."*7)                   # 메시지 출력
    print("철컥! 장전이 완료 되었습니다.") 
    bull = 0
    maxBullet = random.randint(1,4)         # 총 탄수 랜덤값으로 지정
    global bugshot
    bugshot = [0,0,0,0,0,0,0,0]
    while(bull < maxBullet):
        chamber = random.randint(0,7)       # 총 탄수 랜덤값으로 지정
        if bugshot[chamber] == 1 : continue
        else: 
            bugshot[chamber] = 1
            bull += 1

# --------  벅샷 조준, 사격 메서드 -------------------------------------------------------------------------
def aimingBugshot(gunner,target):                  # target(사격자, 타겟)
    print('끼릭 ...... 철컥 !')
    mentKey = abs(player[gunner]['mind']-(gunner - target))
    print(playMent[gunner][mentKey])
    if player[gunner]['mind']:
        if gunner : print('"대체 언제 건거야 ?"')
        else : print('"어... 내가 왜이러지 ?"')
    input()
    if player[gunner]['mind'] :                # 사격자 상태 체크
        print(f'총구가 반대로 이동합니다.{player[target]["name"]}을 조준합니다.')
        player[gunner]['mind'] = 0                 # 플레이어 스텟 클리어
        input()
    if bugshot[0]:                                  # bugshot 리스트 첫번째 값이 1 : 트루일경우
        shotBugshot(gunner,target)                 # 격발 메서드 실행
        return True                                 # 턴 넘김 유무를 위해 값 반환
    else :
        print('틱........................ 격발되지 않았습니다.')
        if player[gunner]['dmg'] != 1 : player[gunner]['dmg'] = 1
        del bugshot[0]
        return False 

# --------  벅샷 격발 유무 메서드 -------------------------------------------------------------------------
def shotBugshot(gunner,target):
    if gunner and not player[1]['brain'] : player[1]['brain'] = 0 # 브레인이 0이 아닐경우 0으로
    player[target]['hp'] -= player[gunner]['dmg']     # 선언된 상대에게 데미지 만큼 마이너스
    if player[gunner]['dmg'] == 1 :
        print(f'탕! - 격발되었습니다. {player[target]["name"]}의 체력이 감소합니다.')
    else:
        print(f'타 - 앙!!! 격발되었습니다. {player[target]["name"]}의 체력이 크게 감소합니다.')
        player[gunner]['dmg'] = 1
    apendItemList(target)
    bugshot.clear() # 벅샷 리스트 값 초기화
    input()
    bugshotSetting() # 다시 장전
    

# -------- 선택지 입력 체크리스트 --------------------------------------------------------------------------
def inputTest(inputData,ch1,ch2):   # String데이터, 범위지정수1, 범위지정수2
    if inputData.isnumeric() :      # 입력된 문자열이 숫자로 구성되어 있는지 확인
        inputData = int(inputData)  # 위가 True라면 int로 형변환
        if ch1 <= inputData <= ch2: # 범위 지정 정수 1,2 사이의 값인지 확인
            return True             # 맞다면 True 반환
    print('입력값이 잘못되었습니다.')
    return False                    # 아닐경우 메시지, False 반환
    
# -------- 리스트 메서드 선언 -----------------------------------------------------------------------------
def showList():
    print(f'{"-"*30} 현재 탄 상황: {len(bugshot)}/{bugshot.count(1)}')
    print(f'{"player님의 차례입니다.".ljust(24)}player hp: {player[0]["hp"]}')
    print(f'{"-"*30} dealer hp: {player[1]["hp"]}')
    print('1. 상대 쏘기')
    print('2. 날 쏘기')
    print('3. 아이템 목록')
    print('4. 항복')
    print('-'*30)

# -------- 컴퓨터 뷰 메서드 선언 ----------------------------------------------------------------------------
def computerView():
    print(f'{"-"*30} 현재 탄 상황: {len(bugshot)}/{bugshot.count(1)}')
    print('딜러가 음흉하게 미소짓고 있습니다.')
    print(f'{"-"*30} player hp: {player[0]["hp"]}')
    print(f'{"-"*30} dealer hp: {player[1]["hp"]}')
    gameMude = player[0]['hp'] - player[1]['hp']# 불리할때 유리할때 판단할 변수
    mentIdx = random.randint(0,1)               # 랜덤으로 멘트를 띄우기 위한 변수
    if(gameMude == 0) : Ment = playMent[1][7+mentIdx]
    elif(gameMude > 0) : Ment = playMent[1][9+mentIdx]
    elif(gameMude < 0) : Ment = playMent[1][11+mentIdx]
    print(f'"{Ment}"')
    print('-'*30)
    
    
# -------- 아이템 리스트 추가 메서드 ------------------------------------------------------------------------
def apendItemList(target): # target : 함수가 사용되는 대상
    print(f'{player[target]["name"]}에게 아이템이 지급됩니다.') 
    player[target]['item'].append(random.randint(0,5))      # 대상 플레이어의 딕셔너리 > 아이템 리스트에 값 추가

# -------- 아이템 리스트 출력 메서드 ------------------------------------------------------------------------
def showItemList(target):
    myItem = [] # 반환할 내 아이템 리스트
    hit = 1 # 반복수(선택하는 숫자 제공)
    for item in player[target]['item']:     # 대상 플레이어의 딕셔너리 > 아이템 리스트의 값의 수만큼 반복
        myItem.append(f'{hit}. {itemName[item]}') # 추가
        hit += 1
    return myItem

# -------- 아이템 맥주 사용 메서드 -------------------------------------------------------------------------
def beerDrink(target):
    print(playMent[target][2])
    print('철컥 ... 드르륵 핑.... 총알이 빠져나갔다!')
    del bugshot[0]                                  # 벅샷 리스트 첫번째 값 제거
    if bugshot.count(1) == 0 or len(bugshot) == 0:  # 만약 마지막 총알이거나 남은 실탄이 없다면 다시 재장전
        print('총알이 비었습니다. 다시 장전 시작합니다.')
        bugshotSetting()

# -------- 아이템 담배 사용 메서드 --------------------------------------------------------------------------
def smokeUp(target):
    print(playMent[target][3])
    player[target]['hp'] += 1       # .... 아이템 리스트 안의 hp값 +1

# -------- 아이템 돋보기 사용 메서드 ------------------------------------------------------------------------
def checkBullet(target):
    print(playMent[target][4])
    print('끼리리리릭 털컥.......')
    if not target : input()
    if bugshot[0] :             # 벅샷 리스트 첫번째 값이 총알이 있는지 검사
        if not target : 
            print('약실에 미세하게 총알이 보인다...')
        if player[1]['brain'] == 0 and target :     # 컴퓨터가 사용하고 만약 브레인이 0인상태면 실행
            if 3 in player[1]['item']: player[1]['brain'] = 3   # 만약 아이템(총기손질)이 있다면 브레인 3으로 변환
            else: player[1]['brain'] = 1            # 아닐경우 1로 변환
    else:
        if not target : 
            print('약실에 아무것도 보이지 않는다.')
            if player[1]['brain'] == 0 and target :
                player[1]['brain'] = 2

# -------- 아이템 총기손질 사용 메서드 -----------------------------------------------------------------------
def upgradeGun(target):
    print('끼이이익.... 불길한 소리가 들린다 ')
    print(playMent[target][5])
    player[target]['dmg'] +=1               # ..... 대상의 dmg 에 1 더하기
    if player[1]['brain'] == 0 and target : player[1]['brain'] = 1

# -------- 아이템 최면 사용 메서드 ---------------------------------------------------------------------------
def hypnosiss(target):
    player[1-target]['mind'] = 1
    if not target : print('상대는 최면에 걸렸다.')  # ..... 대상의 mind 1 : 최면상태로 변환

# -------- 아이템 오함마 사용 메서드 ------------------------------------------------------------------------------
def hammerGrab(target):
    player[1-target]['stat'] = 1                  # ..... 대상의 stat 1 : 오함마 대기로 변환
    if not target : print('오함마를 손에 쥐었다.') 

def hammerSmash(target,idx):                     
    print(playMent[target][6])
    input()
    print('오함마에 걸렸습니다. 아이템사용이 파괴되고 턴이 종료됩니다.')
    del player[target]['item'][idx]               # .... 아이템 리스트 사용한 아이템의 idx 값 삭제
    player[target]['stat'] = 0                    # 대상 스텟 초기화
    global turn
    turn = 1-target

# -------- 컴퓨터 플레이 메서드 ----------------------------------------------------------------------------------
def computerPlay():
    itemRandomStat = random.randint(0,2)                # 아이템 쓸 확률 정하기
    if player[1]['brain'] > 0 : 
        choice = player[1]['brain'] # 탄환이 있을경우 1, 탄환없으면 2, 탄환있고 총기강화 있으면 3
    else:
        # 아이템이 있고 아이템의 개수가 3개 이상이거나 담배가 있다면
        if len(player[1]['item']) and (
            len(player[1]['item']) > 3 or 
            1 in player[1]['item'] or itemRandomStat ) :
            return 3
        if len(bugshot) - bugshot.count(1) < 2:                   # 총 탄창 - 실탄 이 2개 보다 적다면
            choice = 1
        elif bugshot.count(1) > len(bugshot) // 2:                # 총 탄찬 / 2보다 실탄이 많다면
            idx = random.randint(0,2)
            choice = [1,1,2][idx]                                 # 랜덤인자 사격에 보다 집중
        else:
            choice = random.randint(1,2)
    return choice

def computerItemUse():                                     
    itemIdx = 0 # 선택할 아이템 기본값 0
    
    if player[1]['brain'] == 3 :            # 약실에 총알이 있고 총탄강화 아이템이 있을경우
        print('아주 확실한 타이밍이군!')
        itemIdx = 3                         # 총기강화 사용
        player[1]['brain'] == 1             # 무조건 사격으로 변경
    else:
        for i in itemFirst:
            if i in player[1]['item'] :           # 우선도 담배 > 약실확인 > 맥주 > 총기강화
                itemIdx = i
                break
        if itemIdx > 3: 
            player[1]['isView'] = False             # ... isview false로 변환
        else : 
            print('딜러가 자신을 진열장을 열어봅니다')
            print(f'{itemName[itemIdx]}을 사용합니다.')
            input()
    return player[1]['item'].index(itemIdx)+1 # 값 반환

# -------- 아이템 사용 메서드 ------------------------------------------------------------------------------
def useItem(target,num): # 현제 턴 플레이어, 사용할 아이템 번호
    idx = num - 1 # 내 아이템리스트 안의 인덱스 값 계산
    if player[target]['stat'] == 1 :    # 오함마대기중에 아이템을 사용한다면
        hammerSmash(target,idx)      
        return 0                        # 함수 종료
    myItem = player[target]['item'][idx] # myItem ==> 사용할 아이템의 인덱스값
    if not turn :                        # 플레이어 일경우
        print(f'아이템 설명: {itemInfo[myItem]}')
        if not yesOrNo(f'{itemName[myItem]}를 사용하시겠습니까?') : # 함수 YesOrNo 사용 True or False 반환
            print('취소되었습니다.')
            return False # False일 경우 메서드 종료
        
            
    
    # 실행될 함수 리스트 - '맥주마시기','담배','약실확인','총기손질','최면','오함마'
    funcList = [beerDrink, smokeUp, checkBullet, upgradeGun, hypnosiss, hammerGrab]
    funcList[myItem](target) # idx 맞는 함수 실행
    del player[target]['item'][idx] # 사용한 아이템 삭제
def checkList():
    print(player)

bugshotSetting()    # 총 장전
apendItemList(0)    # 초기 아이템 지급
apendItemList(0)
apendItemList(1)
apendItemList(1)
while True :
    result = False
    enemy = 1 - turn # 상대방 구하기
    if player[turn]['hp'] < 1 or player[enemy]['hp'] < 1:       # 플레이어의 체력이 1보다 낮으면
        winnerIdx = 0 if player[0]['hp'] > 0 else 1 
        print(f'{player[winnerIdx]["name"]}의 승리입니다.',sep='') # 승리 발표후 반복종료
        break
    if turn :                       # 컴퓨터인지 검사
        if player[1]['isView'] :
            input()
            computerView()
        else:player[1]['isView'] = True
        playnum = computerPlay()
    else :                          # 플레이어일 경우
        input()
        showList() # 리스트 출력
        playnum = input('1자리 정해진 수만 입력해 주세요(1~4) : ') # 선택지 요청
        if not inputTest(playnum,1,5) : continue        # 조건과 틀릴시 반복 다시실행
        playnum = int(playnum)
        print('-'*30)
    if player[turn]['mind'] and playnum < 3:       # 환각 상태고 사격을 선택했을 경우
        playnum = 3 - playnum                           # 최면상태시 1을 2로 2를 1로 변환

    if playnum == 1:    # 1일경우 상대 플레이어를 대상으로 aimingBugshot 실행
        result = not aimingBugshot(turn,enemy)
    elif playnum == 2:  # 2일경우 현재 플레이어를 대상으로 aimingBugshot 실행
        result = aimingBugshot(turn,turn)
    elif playnum == 3:
        if turn :       # 컴퓨터인 경우
            computerItemIdx = computerItemUse()        # 아이템 유스 함수 실행 반환값이 1추가
            useItem(turn,computerItemIdx)                # useItem통해 아이템 사용
            continue
        else:
            if not len(player[turn]['item']) :
                print('아이템이 없습니다.')
                continue
            while True:
                print('-'*30)
                print(showItemList(turn))  # 자신의 아이템 리스트 출력
                print('-'*30)
                itemNum = input('가방안에 아이템들이 보인다(번호만 입력해주세요) 나가실려면 (N) : ') # 아이템 번호 입력
                if itemNum == 'N' or itemNum =='n' :
                    print('아이템 가방을 닫았다.')
                    break
                else:
                    if not inputTest(itemNum,1,len(player[turn]['item'])) : continue # 조건과 틀릴시 반복 다시실행
                    itemNum = int(itemNum)
                    useItem(turn,itemNum) # 아이템 사용
                    input()
                    continue
            continue
    elif playnum == 4: # 항복시
        if yesOrNo('"정말로 항복이야 시시하구만~" ') :
            player[turn]['hp'] = 0      # 현재 플레이어 hp == 0으로 만들고 반복다시 실행
        else :
            print('다시 정신을 붙잡고 게임을 계속한다')
            print('"겁쟁이는 재미없지! 좋은 생각이야!"')
        continue
    elif playnum == 5:
        checkList()
    player[turn]['stat'] = 0            # 스텟 초기화
    if result : turn = 1-turn           # 턴이 넘어가야할 경우 턴 넘김
    print()
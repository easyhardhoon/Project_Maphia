from random import *
citizens_number = int(input("시민의 수를 입력하세요"))
mapia_number = int(input("마피아의 수를 입력하세요"))
smart_key_for_smartpolice = [-1]

def checking_exist_maphia(array,number_between_citizens_maphias):
    for a in array:
        if(a>number_between_citizens_maphias):
            return True    
    return False
def checking_exist_police(array):
    for a in array:
        if(a == 0):
            return True    
    return False
def checking_exist_citizens(array,number_between_citizens_maphias):
    for a in array:
        if (a<=number_between_citizens_maphias):
            return True
    return False
def set_police_among_citizen(array,citizens_number):
    police = randrange(0,citizens_number)
    array[police] = 0
    return array
#일단 경찰은 '0' 이다

def police_work_uglycase(array,citizens_number):
    #중복 검사 허용하는 ugly 경찰
    print("경찰은 한명을 지목하여 마피아인지 아닌지 확인합니다")
    key = choice(array)
    if (key > citizens_number):
        print("경찰이 지목한 사람은 마피아가 맞습니다")
        target = key
        return target
    else:
        print("경찰이 지목한 사람은 선량한 시민입니다")
        target = 0
        return target

def police_work_smartcase(array,citizens_number):
    #중복 검사 허용하지 않는 경찰.
    #print("경찰은 한명을 지목하여 마피아인지 아닌지 확인합니다")
    while True:
        key = choice(array)
        for smart_key in smart_key_for_smartpolice:
            if key == smart_key: continue
        break
    #중복이 되지 않을때까지 새로운 key 값 입력
    if (key > citizens_number):
        #print("경찰이 지목한 사람은 마피아가 맞습니다")
        target = key
        nn=0
        for smart_key in smart_key_for_smartpolice:
            if key == smart_key:
                nn+=1
        if(nn==0):
            smart_key_for_smartpolice.append(key)
        return target
    else:
        #print("경찰이 지목한 사람은 선량한 시민입니다")
        target = 0
        nn=0
        for smart_key in smart_key_for_smartpolice:
            if key == smart_key:
                nn+=1
        if(nn==0):
            smart_key_for_smartpolice.append(key)
        return target

def first_game_like_real(array,citizens_number):
    array = list(map(str,array))
    for a in range(len(array)):
        if array[a] == "0":
            array[a] = "진혁"
        elif array[a] == "1":
            array[a] = "지훈"
        elif array[a] == "2":
            array[a] = "예훈"
        elif array[a] == "3":
            array[a] = "창한"
        elif array[a] == "4":
            array[a] = "하운"
        elif array[a] == "5":
            array[a] = "정윤"
        elif array[a] == "6":
            array[a] = "민지"
        elif array[a] == "7":
            array[a] = "규식"
        elif array[a] == "8":
            array[a] = "강희"
        elif array[a] == "9":
            array[a] = "길호"
        elif array[a] == "10":
            array[a] = "은지"
    return array
def game_like_real(array,citizens_number):
    array = list(map(str,array))
    for a in range(len(array)):
        if int(array[a]) > citizens_number:
            array[a] = "마피아"
        elif array[a] == "0":
            array[a] = "경찰"
        elif array[a] == "1":
            array[a] = "지훈"
        elif array[a] == "2":
            array[a] = "예훈"
        elif array[a] == "3":
            array[a] = "창한"
        elif array[a] == "4":
            array[a] = "하운"
        elif array[a] == "5":
            array[a] = "정윤"
        elif array[a] == "6":
            array[a] = "민지"
        elif array[a] == "7":
            array[a] = "규식"
        elif array[a] == "8":
            array[a] = "강희"
        elif array[a] == "9":
            array[a] = "길호"
        elif array[a] == "10":
            array[a] = "은지"
    return array
    #언제가는 이 str_Array를 쓸일이 있을까봐...
def game_start(citizens_number,maphia_number):
    date=1
    checking_number = citizens_number
    Citizens = list(range(1,citizens_number+1))
    Mapias = list(range(citizens_number+1,citizens_number + mapia_number+1))
    Gamer = Citizens + Mapias
    #print("참가자 : ",first_game_like_real(Gamer,citizens_number))
    Gamer = set_police_among_citizen(Gamer,citizens_number)
    #print("게임 세팅이 완료되었습니다")
    #print("마피아 게임 시작합니다")
    #print("참가자 : ",game_like_real(Gamer,citizens_number))
    is_exist_citizens = True
    is_exist_maphias = True
    is_exist_police  = True
    target = 0
    #print("\n")
    while(1):
        #print("{}일 낮이 밝았습니다.".format(date))
        die_people = choice(Gamer)
        if (target != 0 and is_exist_police == True):
            Gamer.remove(target)
            target = 0
            #print("경찰의 도움으로 마피아가 투표로 사망했습니다")
        else:
            Gamer.remove(die_people)
            if die_people == 0:
                #print("우리의 경찰이 투표로 사망했습니다")
                is_exist_police = False
            elif die_people <= citizens_number:
                checking_number-=1
                #print("선량한 시민이 투표로 사망했습니다")
            elif die_people > citizens_number:
                pass
                #print("운좋게도 마피아가 투표로 사망했습니다")
        #print("생존자 : ",game_like_real(Gamer,citizens_number))
        is_exist_citizens = checking_exist_citizens(Gamer, citizens_number)
        is_exist_maphias = checking_exist_maphia(Gamer, citizens_number)
        if (is_exist_citizens == False):
            who_is_winner = "maphia"
            break
        elif (is_exist_maphias == False):
            who_is_winner = "citizen"
            break
        #print("{}일 밤이 밝았습니다".format(date))
        if(is_exist_police == True):
            #target = police_work_uglycase(Gamer,citizens_number)
            target = police_work_smartcase(Gamer,citizens_number)
        die_people = choice(Gamer[:checking_number]) 
        checking_number-=1
        Gamer.remove(die_people)
        if die_people == 0:
            #print("우리의 경찰이 마피아의 습격으로 사망했습니다")
            is_exist_police = False
        else:
            #print("선량한 시민이 마피아의 습격으로 사망했습니다")
            pass
        #print("생존자 : ",game_like_real(Gamer,citizens_number))
        #print("\n")
        is_exist_citizens = checking_exist_citizens(Gamer, citizens_number)
        is_exist_maphias = checking_exist_maphia(Gamer, citizens_number)
        if (is_exist_citizens == False):
            who_is_winner = "maphia"
            break
        elif (is_exist_maphias == False):
            who_is_winner = "citizen"
            break
        date+=1
    return who_is_winner

total_citizen_win = 0
total_maphia_win = 0
k = 100000
#k = 1
for i in range(k):
    who_is_winner = game_start(citizens_number, mapia_number)
    if who_is_winner == "maphia":
        total_maphia_win +=1
    else:
        total_citizen_win +=1
    #print("게임이 종료되었습니다")
    #print("{} 팀의 승리입니다".format(who_is_winner))
print("시민팀은 {}번 이겼고 : 마피아팀은 {}번 이겼습니다 ".format(total_citizen_win,total_maphia_win))

#마피아 게임 1단계 알고리즘 구현 완료

#여담이지만 샘플코드와 내 코드의 차이점
#샘플코드는 더 간단할 수 있다
#내 코드로 각 시민들에 이름또는 역할을 부여할 수 있다. 
#아무튼 저녁에 의사,경찰 넣고 게임 돌려보기!!!

#soulution
# 1. 시민 중 한명에게 랜덤으로 경찰의 역할을 부여한다
# 2. 둘째 밤에 경찰은 마피아 채킹을 할 수 있다. (살아있다면)

#[21.11.12] 머리 안좋은 경찰까지 구현완료. 문자열로 바꿔서 사람 이름 넣으면서 함 ㅋㅋ 
#다음에 머리좋은 경찰 + 의사 구현!!!!


#[21.11.17]
#1. 낮에 경찰이 살아있으면!! 전날에 마피아 찾기에 성공했다면 마피아를 투표로 죽일수 있다. ugly 경찰 코드 완성
#2. smart 경찰 구현. 한번 검사한 대상은 다시는 검사하지 않는 경찰 구현해보자
#3. 의사 구현



from random import *
from copy import *
citizens_number = int(input("시민의 수를 입력하세요"))
mapia_number = int(input("마피아의 수를 입력하세요"))
array_for_smartpolice = [0]

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
def checking_exist_doctor(array):
    for a in array:
        if(a == -1):
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
def set_doctor_among_citizen(array, citizens_number):
    while True:
           doctor = randrange(0,citizens_number)
           if array[doctor]  == 0:
               continue
           break
    array[doctor] = -1
    return array
#일단 의사는 '-1'이다
#의사와 경찰이 겹치면 안되는데.....
def police_work_uglycase(array,citizens_number):
    #중복 검사 허용하는 ugly 경찰
    #print("경찰은 한명을 지목하여 마피아인지 아닌지 확인합니다")
    while True:
        key = choice(array)
        if key == 0:
            continue
        break
    #경찰은 자기자신을 지목하지 못한다
    if (key > citizens_number):
        #print("경찰이 지목한 사람은 마피아가 맞습니다")
        target = key
        return target
    else:
        #print("경찰이 지목한 사람은 선량한 시민입니다")
        target = 0
        return target

def police_work_smartcase(array,citizens_number):
    copy_array = deepcopy(array)
    #깊은 복사의 개념. import copy의 deepcopy 함수로 구현
    for smart_key in array_for_smartpolice:
        if(smart_key in copy_array):
            copy_array.remove(smart_key)
    #중복 검사 허용하지 않는 경찰.
    #print("경찰은 한명을 지목하여 마피아인지 아닌지 확인합니다")
    key = choice(copy_array)
    #전체 array에서 smart_key_for_smartpolice 배열을 뺀 배열을 정의하고
    #거기서 고르기. 0이면 다시 하기
    #최초 smart_array에 0을 넣음으로써 remove 에러 안뜨기 & 경찰 자기자신 안고르기 효과 일타이피
    if (key > citizens_number):
        #print("경찰이 지목한 사람은 마피아가 맞습니다")
        target = key
        nn=0
        for smart_key in array_for_smartpolice:
            if key == smart_key:
                nn+=1
        if(nn==0):
            array_for_smartpolice.append(key)
        return target
    else:
        #print("경찰이 지목한 사람은 선량한 시민입니다")
        target = 0
        nn=0
        for smart_key in array_for_smartpolice:
            if key == smart_key:
                nn+=1
        if(nn==0):
            array_for_smartpolice.append(key)
        return target

def doctor_work(array):
    #print("의사는 살릴 대상을 선택합니다")
    saver = choice(array);
    return saver
def first_game_like_real(array,citizens_number):
    array = list(map(str,array))
    for a in range(len(array)):
        if array[a] == "0":
            array[a] = "지훈"
        elif array[a] == "1":
            array[a] = "민찬"
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
            array[a] = "규민"
        elif array[a] == "8":
            array[a] = "지호"
        elif array[a] == "9":
            array[a] = "시영"
        elif array[a] == "10":
            array[a] = "민혁"
        elif array[a] == "11":
            array[a] = "승찬"
        elif array[a] == "12":
            array[a] = "석문"
        elif array[a] == "13":
            array[a] = "서윤"
        elif array[a] == "14":
            array[a] = "준철"
        elif array[a] == "15":
            array[a] = "기훈"

    return array
def game_like_real(array,citizens_number):
    array = list(map(str,array))
    for a in range(len(array)):
        if int(array[a]) > citizens_number:
            array[a] = "마피아"
        elif array[a] == "-1":
            array[a] = "의사"
        elif array[a] == "0":
            array[a] = "경찰"
        elif array[a] == "1":
            array[a] = "민찬"
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
            array[a] = "규민"
        elif array[a] == "8":
            array[a] = "지호"
        elif array[a] == "9":
            array[a] = "시영"
        elif array[a] == "10":
            array[a] = "민혁"
        elif array[a] == "11":
            array[a] = "승찬"
        elif array[a] == "12":
            array[a] = "석문"
        elif array[a] == "13":
            array[a] = "서윤"
        elif array[a] == "14":
            array[a] = "준철"
        elif array[a] == "15":
            array[a] = "기훈"
    return array
    #언제가는 이 str_Array를 쓸일이 있을까봐...
def game_start(citizens_number,maphia_number):
    date=1
    checking_number = citizens_number
    #checking_number가 핵심임. 시민의 수가 줄면 하나씩 줄어든다. 
    Citizens = list(range(1,citizens_number+1))
    Mapias = list(range(citizens_number+1,citizens_number + mapia_number+1))
    Gamer = Citizens + Mapias
    #print("참가자 : ",first_game_like_real(Gamer,citizens_number))
    Gamer = set_police_among_citizen(Gamer,citizens_number)
    #Gamer = set_doctor_among_citizen(Gamer, citizens_number)
    #print("게임 세팅이 완료되었습니다")
    #print("마피아 게임 시작합니다")
    #print("참가자 : ",game_like_real(Gamer,citizens_number))
    is_exist_citizens = True
    is_exist_maphias = True
    is_exist_police  = True
    #is_exist_doctor = True
    target = 0 #임시. 마피아를 찾으면 양의 정수형태로 바뀌게 코드 구현
    saver = -10 #임시. 게임에 버그를 안주기 위해 안쓰는 음수값  하나 선택
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
                #실제 게임에서는 안알려주는게 맞지만 코드의 분석을 위해 사용
                checking_number-=1
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
            target = police_work_uglycase(Gamer,citizens_number)
            #target = police_work_smartcase(Gamer,citizens_number)
        die_people = choice(Gamer[:checking_number]) 
        Gamer.remove(die_people)
        checking_number-=1
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
#k = 100000
k = 10000
#k = 10


#확률 분석 코드. 
for i in range(k):
    who_is_winner = game_start(citizens_number, mapia_number)
    #print(array_for_smartpolice)
    array_for_smartpolice = [0] #smart array를 다시 초기화해줘야 함
    #print(array_for_smartpolice)
    if who_is_winner == "maphia":
        total_maphia_win +=1
    else:
        total_citizen_win +=1
    #print("게임이 종료되었습니다")
    #print("{} 팀의 승리입니다".format(who_is_winner))
print("시민팀은 {}번 이겼고 : 마피아팀은 {}번 이겼습니다 ".format(total_citizen_win,total_maphia_win))





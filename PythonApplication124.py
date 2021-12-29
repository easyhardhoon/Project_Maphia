from random import *
from copy import *
citizens_number = int(input("시민의 수를 입력하세요 : "))
mapia_number = int(input("마피아의 수를 입력하세요 : "))
array_for_smartpolice = [0]
#smart_police을 위한 배열
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
    police = randrange(0,citizens_number) #경찰은 0이다
    array[police] = 0
    return array
def set_doctor_among_citizen(array, citizens_number):
    while True:
           doctor = randrange(0,citizens_number)
           if array[doctor]  == 0: #의사와 경찰이 겹치면 안된다. 의사는 -1이다
               continue
           break
    array[doctor] = -1
    return array
def set_army_among_citizen(array, citizens_number):
    while True:
        army = randrange(0,citizens_number)
        if array[army] == 0 or array[army] == -1: # 군인 의사 경찰이 겹치면 안된다. 군인은 -2이다
            continue
        break
    array[army] = -2
    return array
def set_noble_among_citizen(array, citizens_number):
    while True:
        noble = randrange(0,citizens_number)
        if array[noble] == 0 or array[noble] == -1 or array[noble] == -2: # 귀족 군인 의사 경찰이 겹치면 안된다. 귀족은 -3이다
            continue
        break
    array[noble] = -3
    return array
def police_work_uglycase(array,citizens_number):
    #중복 검사 허용하는 ugly 경찰
    print("경찰은 한명을 지목하여 마피아인지 아닌지 확인합니다")
    while True:
        key = choice(array)
        if key == 0:
            continue #경찰은 자기자신을 지목하지 못한다
        break
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
    copy_array = deepcopy(array)
    #깊은 복사의 개념. import copy의 deepcopy 함수로 구현. 원래 array 값 훼손하지 않기 위해 구현
    for smart_key in array_for_smartpolice:
        if(smart_key in copy_array):
            copy_array.remove(smart_key)
    print("경찰은 한명을 지목하여 마피아인지 아닌지 확인합니다")
    key = choice(copy_array)
    #전체 array에서 smart_key_for_smartpolice 배열을 뺀 배열을 정의
    #최초 smart_array에 0을 넣음으로써 remove 에러 안뜨기 & 경찰 자기자신 안고르기 효과 일타이피
    if (key > citizens_number):
        print("경찰이 지목한 사람은 마피아가 맞습니다")
        target = key
        nn=0
        for smart_key in array_for_smartpolice:
            if key == smart_key:
                nn+=1
        if(nn==0):
            array_for_smartpolice.append(key)
        return target #마피아를 찾으면 마피아를 target에 넣어주고 리턴
    else:
        print("경찰이 지목한 사람은 선량한 시민입니다")
        target = 0
        nn=0
        for smart_key in array_for_smartpolice:
            if key == smart_key:
                nn+=1
        if(nn==0):
            array_for_smartpolice.append(key)
        return target #마피아가 아니면 0값을 target에 넣어주고 리턴

def doctor_work(array):
    print("의사는 살릴 대상을 선택합니다")
    saver = choice(array)
    return saver #살릴 사람 무작위 선택(자기자신 포함)
def army_work(army_life):
    army_life=1
    return army_life #군인 생명 하나 단축
def noble_work(noble_life):
    noble_life=1
    return noble_life #의사 생명 하나 단축
def is_target_maphia(target):
    if target == 0:
        return False
    else:
        return True
def die_people_name(die_people,citizens_number):
    if die_people == -3:
        result = "귀족"
        return result
    elif die_people == -2:
        result = "군인"
        return result
    elif die_people == -1:
        result = "의사"
        return result
    elif die_people == 0:
        result = "경찰"
        return result
    elif die_people <= citizens_number:
        result = "시민"
        return result
    else:
        result = "마피아"
        return result
    
def first_game_like_real(array,citizens_number): #실제 이름을 넣어주어 실감나게 구현
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
def game_like_real(array,citizens_number): #실제 이름을 넣어주어 실감나게 구현
    array = list(map(str,array))
    for a in range(len(array)):
        if int(array[a]) > citizens_number:
            array[a] = "마피아"
        elif array[a] == "-3":
            array[a] = "귀족"
        elif array[a] == "-2":
            array[a] = "군인"
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
def smart_maphia_END_AT_DAY(checking_number,Gamer):
    if checking_number == len(Gamer)-checking_number:
        return True
    else:
        return False
def game_start(citizens_number,maphia_number):
    date=1
    checking_number = citizens_number
    #checking_number : 시민의 수가 줄면 하나씩 줄어든다. 마피아가 밤에 시민을 찾아 죽일때 사용
    Citizens = list(range(1,citizens_number+1))
    Mapias = list(range(citizens_number+1,citizens_number + mapia_number+1))
    Gamer = Citizens + Mapias
    print("참가자 : ",first_game_like_real(Gamer,citizens_number))
    Gamer = set_police_among_citizen(Gamer,citizens_number)
    Gamer = set_doctor_among_citizen(Gamer, citizens_number)
    Gamer = set_army_among_citizen(Gamer,citizens_number)
    Gamer = set_noble_among_citizen(Gamer,citizens_number)
    print("게임 세팅이 완료되었습니다")
    print("마피아 게임 시작합니다")
    print("참가자 : ",game_like_real(Gamer,citizens_number))
    is_exist_citizens = True
    is_exist_maphias = True
    is_exist_police  = True
    is_exist_doctor = True
    target = 0 #임시. 마피아를 찾으면 양의 정수형태로 바뀌게 코드 구현
    saver = -10 #임시. 게임에 버그를 안주기 위해 안쓰는 음수값 하나 선택
    army_life = 2 #군인의 목숨
    noble_life = 2 #귀족의 목숨
    print("\n")
    while(1):
        print("{}일 낮이 밝았습니다.".format(date))
        if smart_maphia_END_AT_DAY(checking_number,Gamer):
            print("마피아의 수와 시민의 수가 동률입니다. 마피아의 승리입니다.")
            who_is_winner = "maphia"
            break
        die_people = choice(Gamer)
        if ((is_target_maphia(target) == True) and (is_exist_police == True)): #경찰이 아직 살아있고 전날에 찾은 target이 마피아일때 발동
            Gamer.remove(target)
            target = 0
            print("경찰의 도움으로 마피아가 투표로 사망했습니다")
        else:
            if(die_people_name(die_people,citizens_number) == "귀족" and noble_life == 2): #귀족의 목숨이 2개일때만 발동
                noble_life = noble_work(noble_life)
                print("귀족의 능력으로 투표로 죽지않았습니다 (이제 귀족의 능력은 소멸됩니다)")
            else:
                Gamer.remove(die_people)
                if die_people_name(die_people,citizens_number) == "의사":
                    print("우리의 의사가 투표로 사망했습니다")
                    #실제 게임에서는 안알려주는게 맞지만 코드의 분석을 위해 사용
                    checking_number-=1 #시민의 수가 줄면 checking_number도 이에 맞게 감소해야함
                    is_exist_doctor = False
                elif die_people_name(die_people,citizens_number) == "경찰":
                    print("우리의 경찰이 투표로 사망했습니다")
                    #실제 게임에서는 안알려주는게 맞지만 코드의 분석을 위해 사용
                    checking_number-=1
                    is_exist_police = False
                elif die_people_name(die_people,citizens_number) == "군인":
                    print("우리의 군인이 투표로 사망했습니다")
                    checking_number-=1
                elif die_people_name(die_people,citizens_number) == "귀족":
                    print("우리의 귀족이 능력을 소멸하여 투표로 사망했습니다")
                    checking_number-=1
                elif die_people_name(die_people,citizens_number) == "시민":
                    checking_number-=1
                    print("선량한 시민이 투표로 사망했습니다")
                elif die_people_name(die_people,citizens_number) == "마피아":
                    #pass
                    print("운좋게도 마피아가 투표로 사망했습니다")
        print("생존자 : ",game_like_real(Gamer,citizens_number))
        is_exist_citizens = checking_exist_citizens(Gamer, citizens_number)
        is_exist_maphias = checking_exist_maphia(Gamer, citizens_number)
        if (is_exist_citizens == False): #투표로 인해 시민이 전멸하면 바로 게임종료
            who_is_winner = "maphia"
            break
        elif (is_exist_maphias == False): #투표로 인해 마피아가 전멸하면 바로 게임종료
            who_is_winner = "citizen"
            break
        print("{}일 밤이 밝았습니다".format(date))
        if(is_exist_police == True): 
            #target = police_work_uglycase(Gamer,citizens_number) 
            target = police_work_smartcase(Gamer,citizens_number)
        die_people = choice(Gamer[:checking_number]) #checking_number로 인해 올바르게 시민만 찾아 죽일 수 있음
        if(is_exist_doctor == True):
            saver = doctor_work(Gamer) #의사가 살릴 대상 saver에 저장
        if (saver == die_people):
            print("의사의 도움으로 극적으로 살아났습니다")
            saver = -10
        else:
            if die_people_name(die_people,citizens_number) == "군인" and army_life == 2:
                army_life = army_work(army_life)
                print("군인의 능력으로 마피아의 습격을 견뎠습니다(이제 군인의 능력은 소멸됩니다)")
                saver = -10
                #의사의 능력을 우선순위로 책정하기 위해 군인의 능력을 else에 배치
            else:
                Gamer.remove(die_people)
                checking_number-=1
                saver = -10
                if die_people_name(die_people,citizens_number) == "의사":
                    print("우리의 의사가 마피아의 습격으로 사망했습니다")
                    #실제 게임에서는 안알려주는게 맞지만 코드의 분석을 위해 사용
                    is_exist_doctor = False
                elif die_people_name(die_people,citizens_number) == "군인":
                    #pass
                    print("우리의 군인이 능력을 소멸하여 마피아의 습격으로 사망했습니다")
                elif die_people_name(die_people,citizens_number) == "경찰":
                    print("우리의 경찰이 마피아의 습격으로 사망했습니다")
                    is_exist_police = False
                elif die_people_name(die_people,citizens_number) == "귀족":
                    #pass
                    print("우리의 귀족이 마피아의 습격으로 사망했습니다")
                else:
                    print("선량한 시민이 마피아의 습격으로 사망했습니다")
                    #pass
        print("생존자 : ",game_like_real(Gamer,citizens_number))
        print("\n")
        is_exist_citizens = checking_exist_citizens(Gamer, citizens_number)
        is_exist_maphias = checking_exist_maphia(Gamer, citizens_number)
        if (is_exist_citizens == False): #마피아의 습격으로 시민이 전멸하면 break
            who_is_winner = "maphia"
            break
        elif (is_exist_maphias == False): #사실 필요없을듯
            who_is_winner = "citizen"
            break
        date+=1 # 실제 게임처럼 구현하기 위해 day 도입
    return who_is_winner #while 무한루프를 빠져나와 최종적으로 who_is_winner를 리턴 

total_citizen_win = 0
total_maphia_win = 0
#k = 100000
k = 1
#확률 분석 코드. 최대한 정확한 값을 얻기 위해 10만번 돌림
for i in range(k):
    who_is_winner = game_start(citizens_number, mapia_number)
    array_for_smartpolice = [0] #array를 다시 초기화해줘야 함
    if who_is_winner == "maphia":
        total_maphia_win +=1
    else:
        total_citizen_win +=1
    print("게임이 종료되었습니다")
    print("{} 팀의 승리입니다".format(who_is_winner))
#print("시민팀은 {}번 이겼고 : 마피아팀은 {}번 이겼습니다 ".format(total_citizen_win,total_maphia_win))





#마피아 프로젝트 보완 프로젝트
# 21.12.28 : 가독성 높이는 함수 2개 사용.
# 21.12.29 : 낮에 (투표하기 전) 마피아 수와 시민의 수가 같아버리면 게임이 끝나버리는게 상식상 맞다
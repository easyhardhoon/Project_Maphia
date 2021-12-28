from random import *
citizens_number = int(input("시민의 수를 입력하세요"))
mapia_number = int(input("마피아의 수를 입력하세요"))

def checking_exist_maphia(array,number_between_citizens_maphias):
    for a in array:
        if(a>number_between_citizens_maphias):
            return True    
    return False

def checking_exist_citizens(array,number_between_citizens_maphias):
    for a in array:
        if (a<=number_between_citizens_maphias):
            return True
    return False

def game_start(citizens_number,maphia_number):
    date=1
    checking_number = citizens_number
    Citizens = list(range(1,citizens_number+1))
    Mapias = list(range(citizens_number+1,citizens_number + mapia_number+1))
    Gamer = Citizens + Mapias
    print("게임 세팅이 완료되었습니다")
    print("마피아 게임 시작합니다")
    while(1):
        is_exist_citizens = True
        is_exist_maphias = True
        print("{}일 낮이 밝았습니다.".format(date))
        die_people = choice(Gamer)
        Gamer.remove(die_people)
        if die_people <= citizens_number:
            checking_number-=1
            print("선량한 시민이 투표로 사망했습니다")
        else:
            #pass
            print("마피아가 투표로 사망했습니다")
        print(Gamer)
        is_exist_citizens = checking_exist_citizens(Gamer, citizens_number)
        is_exist_maphias = checking_exist_maphia(Gamer, citizens_number)
        if (is_exist_citizens == False):
            who_is_winner = "maphia"
            break
        elif (is_exist_maphias == False):
            who_is_winner = "citizen"
            break
        print("{}일 밤이 밝았습니다".format(date))
        die_people = choice(Gamer[:checking_number]) 
        checking_number-=1
        Gamer.remove(die_people)
        print("선량한 시민이 마피아의 습격으로 사망했습니다")
        print(Gamer)
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
k = 1
for a in range(k):
    who_is_winner = game_start(citizens_number, mapia_number)
    if who_is_winner == "maphia":
        total_maphia_win +=1
    else:
        total_citizen_win +=1
    print("게임이 종료되었습니다")
    print("{} 팀의 승리입니다".format(who_is_winner))
#print("시민팀은 {}번 이겼고 : 마피아팀은 {}번 이겼습니다 ".format(total_citizen_win,total_maphia_win))

#마피아 게임 1단계 알고리즘 구현 완료

#여담이지만 샘플코드와 내 코드의 차이점
#샘플코드는 더 간단할 수 있다
#내 코드로 각 시민들에 이름또는 역할을 부여할 수 있다. 
#아무튼 저녁에 의사,경찰 넣고 게임 돌려보기!!!



from random import *
citizens_number = int(input("시민의 수를 입력하세요"))
mapia_number = int(input("마피아의 수를 입력하세요"))

Citizens = list(range(1,citizens_number+1))
Mapias = list(range(citizens_number+1,citizens_number + mapia_number+1))
Gamer = Citizens + Mapias
print(Citizens)
print(Mapias)
print(Gamer)
print("게임 세팅이 완료되었습니다")
print("마피아 게임 시작합니다")


#그래서 무슨 조건을 만족해야 게임이 끝나지?
#낮에 게임이 끝날 경우. 밤에 게임이 끝날 경우
# 상식상으로는 시민의 수와 마피아의 수가 같으면 게임이 끝나지만
# 여기서는 낮에도 마피아가 마피아를 죽일 수 있기 떄문에 어긋난다
# 체킹 포인트를 둬야할듯. ex) citizen_number. 이 값 기준 작으면 시민 크면 마피아

# 게임이 끝날 조건
# 1. 시민 승 : gamer 속 오직 시민만 존재 
# 2. 마피아 승 : gamer 속 오직 마피아만 존재
def checking_exist_maphia(array,number):
    for a in array:
        if(a>number):
            return True    
    return False
def checking_exist_citizens(array,number):
    for a in array:
        if (a<=number):
            return True
    return False
def game_start(citizens_number):
    a=1
    checking_number = citizens_number
    while(1):
        is_exist_citizens = True
        is_exist_maphias = True
        print("{}일 낮이 밝았습니다.".format(a))
        die_people = choice(Gamer)
        Gamer.remove(die_people)
        if die_people <= citizens_number:
            checking_number-=1
            print("선량한 시민이 투표로 사망했습니다")
        else:
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
        print("{}일 밤이 밝았습니다".format(a))
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
        a+=1
    return who_is_winner
who_is_winner = game_start(citizens_number)
print("게임이 종료되었습니다")
print("{} 팀의 승리입니다".format(who_is_winner))
#마피아 게임 1단계 알고리즘 구현 완료


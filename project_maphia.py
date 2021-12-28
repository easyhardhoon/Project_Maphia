from random import *
citizens_number = int(input("시민의 수를 입력하세요"))
mapia_number = int(input("마피아의 수를 입력하세요"))

Citizens = list(range(1,citizens_number+1))
Mapias = list(range(citizens_number+1,citizens_number + mapia_number+1))
Game_partitions = Citizens + Mapias
print(Citizens)
print(Mapias)
print(Game_partitions)
print("게임 세팅이 완료되었습니다")
print("마피아 게임 시작합니다")

print("1D_m")
die_people = choice(Game_partitions)
Game_partitions.remove(die_people)
print(Game_partitions)
print("1D_n")
die_people = choice(Game_partitions[:citizens_number+1])
Game_partitions.remove(die_people)
print(Game_partitions)
#그래서 무슨 조건을 만족해야 게임이 끝나지?
#낮에 게임이 끝날 경우. 밤에 게임이 끝날 경우
# 상식상으로는 시민의 수와 마피아의 수가 같으면 게임이 끝나지만
# 여기서는 낮에도 마피아가 마피아를 죽일 수 있기 떄문에 어긋난다
# 체킹 포인트를 둬야할듯. ex) citizen_number. 이 값 기준 작으면 시민 크면 마피아
print("sd")







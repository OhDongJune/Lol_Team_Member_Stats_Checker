from Get_driver import Get_driver_class
from Get_Names_Of_All_Summoners import Get_Names_Of_All_Summoners_class
from Get_Info_Of_All_Summoners import Get_Info_Of_All_Summoners_class
from Main_Thread import Main
import threading

def Main():
    # 소환사 이름 입력 및 webdriver 로딩
    name = input('입력하세요 : ')
    name_of_info = input('어떤걸 가져오시겠습니까?(1:이름만, 2:모든 정보) : ')
    # Get_driver_method -> 1 : headless 옵션으로 webdriver 호출, 0 : 일반 webdriver 호출
    driver = Get_driver_class.Get_driver_method(1)
    if name_of_info == '1':
        # 소환사들의 이름 가져오는 부분
        ap = Get_Names_Of_All_Summoners_class.Get_Names_Of_All_Summoners_From_Fow(driver, name)
        # 게임중이 아닐 경우
        if len(ap) == 1:
            print(ap[0])
            return
        # 게임중일 경우
        friendly_players_name = [ap[i] for i in range(0, 5)]
        enemy_players_name = [ap[i] for i in range(5, 10)]
        print('==아군==')
        for name in friendly_players_name:
            print(name+'님이 로비에 참가하셨습니다.')
        print('==적군==')
        for name in enemy_players_name:
            print(name + '님이 로비에 참가하셨습니다.')
    else:
        # 게임 중인 소환사 전원의 정보를 가져온다.
        team_Players_Info = Get_Info_Of_All_Summoners_class.Get_Info_Of_All_Summoners_From_Fow(driver, name)
        # 게임 중이 아님
        if team_Players_Info is None:
            pass
        # 게임 중임
        else:
            for identity in team_Players_Info.keys():
                print('<'+identity+'>')
                for name in team_Players_Info[identity].keys():
                    print(name, end=' : ')
                    print(team_Players_Info[identity][name])

if __name__ == "__main__":
    Main()

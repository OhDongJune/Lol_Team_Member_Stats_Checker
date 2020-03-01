from Get_driver import Get_driver_class
from Get_Names_Of_All_Summoners import Get_Names_Of_All_Summoners_class
from Get_Info_Of_All_Summoners import Get_Info_Of_All_Summoners_class
from Stats_Refresher import Stats_Refresher_class
from Team_Members_Stats_Checker import Team_members_stats_checker_class
from Open_Fow_OPGG import Open_Fow_OPGG_class
import threading

def Main():

    # 소환사 이름 입력
    name = input('입력하세요 : ')
    print('')

    # Get_driver_method -> 1 : headless 옵션으로 webdriver 호출, 0 : 일반 webdriver 호출
    driver = Get_driver_class.Get_driver_method(1)
    driver_fow = Get_driver_class.Get_driver_method(1)

    # 소환사들의 이름 가져오는 부분
    ap = Get_Names_Of_All_Summoners_class.Get_Names_Of_All_Summoners_From_Fow(driver, name)

    # 게임중이 아닐 경우
    if len(ap) == 1:
        print(ap[0])
        return

    blue_team_players_name = [ap[i] for i in range(0, 5)]
    red_team_players_name = [ap[i] for i in range(5, 10)]

    # OPGG, FOW 멀티서치
    # Open_Fow_OPGG_class.Open_Fow_OPGG_method(blue_team_players_name)
    # Open_Fow_OPGG_class.Open_Fow_OPGG_method(red_team_players_name)

    # 게임중일 경우
    """
    print('==아군==')
    for name in blue_team_players_name:
        print(name+'님이 로비에 참가하셨습니다.')
    print('')
    
    print('==적군==')
    for name in red_team_players_name:
        print(name + '님이 로비에 참가하셨습니다.')
    print('')
    """
    team_Players_Info = dict()
    # 게임 중인 소환사 전원의 정보를 가져온다.
    team_Players_Info['Blue Team'] = Get_Info_Of_All_Summoners_class.Get_Info_Of_All_Summoners_From_Fow(driver, name, 'blue')
    team_Players_Info['Red Team'] = Get_Info_Of_All_Summoners_class.Get_Info_Of_All_Summoners_From_Fow(driver, name, 'red')
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
            print('')

    driver_yourgg = driver

    th_yourgg = threading.Thread(target=Stats_Refresher_class.YOURGG_Stats_Refresher, name='[YOURGG THREAD]',
                                 args=(ap, driver_yourgg))
    th_fow = threading.Thread(target=Stats_Refresher_class.Fow_Stats_Refresher, name='[FOW THREAD]',
                              args=(ap, driver_fow))

    # 쓰레드 실행
    th_yourgg.start()
    th_fow.start()

    # 쓰레드 종료 대기
    th_yourgg.join()
    th_fow.join()

    # 쓰레드 종료
    Get_driver_class.Close_driver(driver_fow)
    print('')

    print('<Blue Team>')
    # Blue Team YOURGG 솔로랭크 최근 10게임 평가정보 가져오기
    Team_members_stats_checker_class.last10_days_stats(blue_team_players_name, driver_yourgg)
    print('<Red Team>')
    # Red Team YOURGG 솔로랭크 최근 10게임 평가정보 가져오기
    Team_members_stats_checker_class.last10_days_stats(red_team_players_name, driver_yourgg)

    print('<Blue Team>')
    # Blue Team YOURGG 모든 솔로랭크 평가정보 가져오기
    Team_members_stats_checker_class.total_stats(blue_team_players_name, driver_yourgg)
    print('<Red Team>')
    # Red Team YOURGG 모든 솔로랭크 평가정보 가져오기
    Team_members_stats_checker_class.total_stats(red_team_players_name, driver_yourgg)

    # 쓰레드 종료
    Get_driver_class.Close_driver(driver_yourgg)

if __name__ == "__main__":
    Main()

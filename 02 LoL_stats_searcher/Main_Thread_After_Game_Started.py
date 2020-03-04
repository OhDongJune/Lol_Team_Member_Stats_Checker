from Get_driver import Get_driver_class
from Get_Names_Of_All_Summoners import Get_Names_Of_All_Summoners_class
from Get_Info_Of_All_Summoners import Get_Info_Of_All_Summoners_class
from Stats_Refresher import Stats_Refresher_class
from Team_Members_Stats_Checker import Team_members_stats_checker_class
from OPGG_ban_champion_getter import OPGG_ban_champion_getter_class
from Open_Fow_OPGG import Open_Fow_OPGG_class
from threading import Thread

def Main():

    # 소환사 이름 입력
    name = input('입력하세요 : ')
    print('')

    # Get_driver_method -> 1 : headless 옵션으로 webdriver 호출, 0 : 일반 webdriver 호출
    driver = Get_driver_class.Get_driver_method(1)

    # 게임중이 아니라면 종료한다.
    if Get_Info_Of_All_Summoners_class.isGaming(driver, name) == False:
        return

    # 현재 게임의 종류를 출력한다.
    print('=='+OPGG_ban_champion_getter_class.Get_OPGG_Title(driver, name)+'==')
    print('')

    team_Players_Info = dict()
    # 게임 중인 소환사 전원의 정보를 가져온다.
    team_Players_Info['Blue Team'] = Get_Info_Of_All_Summoners_class.Get_Info_Of_All_Summoners_From_Fow(driver, name, 'blue')
    team_Players_Info['Red Team'] = Get_Info_Of_All_Summoners_class.Get_Info_Of_All_Summoners_From_Fow(driver, name, 'red')

    # 소환사들의 이름을 저장할 딕셔너리
    blue_team_players_dict = dict()
    red_team_players_dict = dict()

    for identity in team_Players_Info.keys():
        print('<'+identity+'>')
        for name in team_Players_Info[identity].keys():
            print(name, end=' : ')
            print(team_Players_Info[identity].get(name))
            if identity == 'Blue Team':
                blue_team_players_dict[name] = team_Players_Info[identity][name].get('챔피언')
            elif identity == 'Red Team':
                red_team_players_dict[name] = team_Players_Info[identity][name].get('챔피언')
        print('')

    # 모든 소환사의 이름
    all_players_name = Get_Names_Of_All_Summoners_class.Get_Names_Of_All_Summoners_From_Fow(driver, name)

    # YOURGG를 업데이트 한다.
    Stats_Refresher_class.YOURGG_Stats_Refresher(all_players_name, driver)
    print('')

    print("==솔로랭크 최근 10게임 평가정보==")

    # Blue Team YOURGG 솔로랭크 최근 10게임 평가정보 가져오기
    se = Team_members_stats_checker_class.last10_days_stats(blue_team_players_dict, driver, 'after')
    # 정보 출력
    print('<Blue Team>')
    Team_members_stats_checker_class.Stats_Print(se, ['전투', '생존', '성장', '시야', '오브젝트', '최근 경기일'])
    print('')

    # Red Team YOURGG 솔로랭크 최근 10게임 평가정보 가져오기
    se = Team_members_stats_checker_class.last10_days_stats(red_team_players_dict, driver, 'after')
    # 정보 출력
    print('<Red Team>')
    Team_members_stats_checker_class.Stats_Print(se, ['전투', '생존', '성장', '시야', '오브젝트', '최근 경기일'])
    print('')

    print("==솔로랭크 모든 게임의 평가정보==")

    # Blue Team YOURGG 모든 솔로랭크 평가정보 가져오기
    se = Team_members_stats_checker_class.total_stats(blue_team_players_dict, driver, 'after')
    # 정보 출력
    print('<Blue Team>')
    Team_members_stats_checker_class.Stats_Print(se, ['전투', '생존', '성장', '시야', '오브젝트'])
    print('')

    # Red Team YOURGG 모든 솔로랭크 평가정보 가져오기
    se = Team_members_stats_checker_class.total_stats(red_team_players_dict, driver, 'after')
    # 정보 출력
    print('<Red Team>')
    Team_members_stats_checker_class.Stats_Print(se, ['전투', '생존', '성장', '시야', '오브젝트'])
    print('')

    # 쓰레드 종료
    Get_driver_class.Close_driver(driver)

if __name__ == "__main__":
    Main()

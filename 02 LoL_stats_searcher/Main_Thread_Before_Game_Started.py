from Get_driver import Get_driver_class
from Summoner_Name_Getter import name_getter
from Stats_Refresher import Stats_Refresher_class
from Team_Members_Stats_Checker import Team_members_stats_checker_class
from Open_Fow_OPGG import Open_Fow_OPGG_class
from threading import Thread

def Main():
    # 소환사 이름 가져오는 부분
    summoners_name = name_getter.name_extractor(0)
    print('소환사 목록 : ', end='')
    print(summoners_name, end='\n\n')

    # 소환사 이름 추가하는 부분
    name_getter.name_adder(summoners_name)
    print('\n소환사 목록 : ', end='')
    print(summoners_name, end='\n\n')

    # OPGG, FOW 멀티서치
    Open_Fow_OPGG_class.Open_Fow_OPGG_method(summoners_name, 1)

    # Get_driver_method -> 1 : headless 옵션으로 webdriver 호출, 0 : 일반 webdriver 호출
    # FOW,OPGG,YOURGG 동시에 전적 업데이트
    driver_fow = Get_driver_class.Get_driver_method(1)
    driver_opgg = Get_driver_class.Get_driver_method(1)
    driver_yourgg = Get_driver_class.Get_driver_method(1)
    driver_last_10_game = driver_fow
    driver_total_game = driver_yourgg

    th_yourgg = Thread(target=Stats_Refresher_class.YOURGG_Stats_Refresher, name='[YOURGG THREAD]',
                                 args=(summoners_name, driver_yourgg))
    th_opgg = Thread(target=Stats_Refresher_class.OPGG_Stats_Refresher, name='[OPGG THREAD]',
                               args=(summoners_name, driver_opgg))
    th_fow = Thread(target=Stats_Refresher_class.Fow_Stats_Refresher, name='[FOW THREAD]',
                              args=(summoners_name, driver_fow))

    # 쓰레드 실행
    th_yourgg.start()
    th_opgg.start()
    th_fow.start()

    # 쓰레드 종료 대기
    th_yourgg.join()
    th_opgg.join()
    th_fow.join()

    # 소환사들 이름 딕셔너리에 추가
    summoners_name_dict = dict.fromkeys(summoners_name)

    # YOURGG에서 최근 10게임 스탯과 모든 게임 스탯을 가져옴
    summoners_last10_days_stats = Team_members_stats_checker_class.last10_days_stats(summoners_name_dict, driver_last_10_game, 'before')
    summoners_total_stats = Team_members_stats_checker_class.total_stats(summoners_name_dict, driver_total_game, 'before')

    print("\n==솔로랭크 최근 10게임 평가정보==")
    Team_members_stats_checker_class.Stats_Print(summoners_last10_days_stats, ['전투', '생존', '성장', '시야', '오브젝트', '최근 경기일'])
    print("\n==솔로랭크 모든 게임의 평가정보==")
    Team_members_stats_checker_class.Stats_Print(summoners_total_stats, ['전투', '생존', '성장', '시야', '오브젝트'])

    # 쓰레드 종료
    Get_driver_class.Close_driver(driver_fow)
    Get_driver_class.Close_driver(driver_opgg)
    Get_driver_class.Close_driver(driver_yourgg)

if __name__ == "__main__":
    Main()

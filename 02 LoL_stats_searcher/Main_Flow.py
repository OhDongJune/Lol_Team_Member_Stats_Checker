from Get_driver import Get_driver_class
from Summoner_Name_Getter import name_getter
from Stats_Refresher import Stats_Refresher_class
from Team_Members_Stats_Checker import Team_members_stats_checker_class
from Open_Fow_OPGG import Open_Fow_OPGG_class
import threading
from selenium.common.exceptions import UnexpectedAlertPresentException

# 소환사 이름 가져오는 부분
summoners_name = name_getter.name_extractor(0)
print('소환사 목록 : ', end='')
print(summoners_name, end='\n\n')

# 소환사 이름 추가하는 부분
name_getter.name_adder(summoners_name)
print('\n소환사 목록 : ', end='')
print(summoners_name, end='\n\n')

# Get_driver_method -> 1 : headless 옵션으로 webdriver 호출, 0 : 일반 webdriver 호출
# headless 옵션으로 webdriver 호출
driver = Get_driver_class.Get_driver_method(1)

# FOW 전적갱신
Stats_Refresher_class.Fow_Stats_Refresher(summoners_name, driver)
print('')

# OPGG 전적갱신
Stats_Refresher_class.OPGG_Stats_Refresher(summoners_name, driver)
print('')

# YOURGG 전적갱신
Stats_Refresher_class.YOURGG_Stats_Refresher(summoners_name, driver)
print('')

# YOURGG 솔로랭크 최근 10게임 평가정보 가져오기
Team_members_stats_checker_class.last10_days_stats(summoners_name, driver)
print('')

# YOURGG 모든 솔로랭크 평가정보 가져오기
Team_members_stats_checker_class.total_stats(summoners_name, driver)
print('')

# 드라이버 종료
driver.close()

# OPGG, FOW 멀티서치
Open_Fow_OPGG_class.Open_Fow_OPGG_method(summoners_name)


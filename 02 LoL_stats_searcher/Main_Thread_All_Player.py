from Get_driver import Get_driver_class
from Get_Names_Of_All_Summoners import Get_Names_Of_All_Summoners_class
from Main_Thread import Main
import threading

def Main():
    # 소환사 이름 입력 및 webdriver 로딩
    name = input('입력하세요 : ')
    # Get_driver_method -> 1 : headless 옵션으로 webdriver 호출, 0 : 일반 webdriver 호출
    driver = Get_driver_class.Get_driver_method(1)
    # 소환사들의 이름 가져오는 부분
    ap = Get_Names_Of_All_Summoners_class.Get_Names_Of_All_Summoners_From_Fow(driver, name)
    # 게임중이 아닐 경우
    if len(ap) == 1:
        print(ap[0])
        return
    # 게임중일 경우
    friendly_player = [ap[i] for i in range(0, 5)]
    enemy_player = [ap[i] for i in range(6, 10)]
    print(friendly_player)
    print(enemy_player)

if __name__ == "__main__":
    Main()

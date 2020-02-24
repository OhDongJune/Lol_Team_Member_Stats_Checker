from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class Get_Info_Of_All_Summoners_class():
    def Get_Info_Of_All_Summoners_From_Fow(driver, name):
        url = 'http://fow.kr/find/' + name
        friendlys_Players_Info = dict()
        enemies_Players_Info = dict()
        team_Players_Info = dict()
        driver.get(url)
        driver.implicitly_wait(10)
        while (True):
            try:
                driver.find_element_by_xpath('//a[@tipsy="진행중인 게임에 대한 정보를 볼 수 있습니다."]/span/b').click()
                driver.implicitly_wait(10)
                buffer = driver.find_element_by_xpath('//div[@class="specinfo"]/div').text
                driver.implicitly_wait(10)
                if buffer == '':
                    continue
                else:
                    break
            except NoSuchElementException:
                continue
        # 게임 중이 아님
        if buffer.find('관전하기') == -1:
            print(buffer)
            return None
        # 게임 중임
        else:
            # print('\n==아군==\n')
            # 아군 소환사 5명의 정보가 있는 부분
            friendlys = driver.find_elements_by_xpath('//td[@style="background-color:#DDF;"]/div')
            for i in range(0, 5):
                summoner_info = dict()
                # 아군 소환사의 정보 7개
                friendly_info = friendlys[i].find_elements_by_tag_name('div')
                # 6번의 b태그의 text : 소환사 이름
                summoner_name = friendly_info[6].find_element_by_tag_name('b').text
                # print(summoner_name, end=' / ')
                # 2번의 tipsy : 챔피언 이름
                champion_name = friendly_info[1].get_attribute('tipsy')
                # print(champion_name, end=' / ')
                summoner_info['챔피언'] = champion_name
                # 6번의 span태그의 text : 챔피언 게임 수, 챔피언 승률, 챔피언 KDA
                champion_info = friendly_info[6].find_element_by_tag_name('span').text.replace(champion_name + ' ', '')
                # 챔피언 게임 수
                champion_played = champion_info[:champion_info.find(' ')]
                # 만약 언랭이면 소환사 정보가 없기 때문에 다음 코드를 실행하지 않는다.
                if champion_played != '':
                    # print(champion_played, end=' / ')
                    summoner_info['판 수'] = champion_played
                    while(True):
                        try:
                            # 챔피언 승률 + KDA
                            win_rate_n_kda = friendly_info[6].find_element_by_tag_name('span').find_elements_by_tag_name('span')
                            break
                        except StaleElementReferenceException:
                            print('StaleElement에러')
                            continue
                    # 챔피언 승률
                    champion_win_rate = win_rate_n_kda[0].text.strip().replace('%', '')
                    # print(champion_win_rate, end=' / ')
                    summoner_info['승률'] = champion_win_rate
                    # 챔피언 KDA
                    champion_kda = win_rate_n_kda[1].text.strip()
                    # print(champion_kda)
                    summoner_info['KDA'] = champion_kda
                else:
                    # champion_played = 'Unrank'
                    summoner_info['판 수'] = 'Unrank'
                    # champion_win_rate = 'Unrank'
                    summoner_info['승률'] = 'Unrank'
                    # champion_kda = 'Unrank'
                    summoner_info['KDA'] = 'Unrank'
                    # print('Unrank')
                friendlys_Players_Info[summoner_name] = summoner_info
            team_Players_Info['Friendly'] = friendlys_Players_Info

            # print('\n==적군==\n')
            # 적군 소환사 5명의 정보가 있는 부분
            enemys = driver.find_elements_by_xpath('//td[@style="background-color:#EDF;"]/div')
            for i in range(0, 5):
                summoner_info = dict()
                # 아군 소환사의 정보 7개
                enemy_info = enemys[i].find_elements_by_tag_name('div')
                # 6번의 b태그의 text : 소환사 이름
                summoner_name = enemy_info[6].find_element_by_tag_name('b').text
                # print(summoner_name, end=' / ')
                # 2번의 tipsy : 챔피언 이름
                champion_name = enemy_info[1].get_attribute('tipsy')
                # print(champion_name, end=' / ')
                summoner_info['챔피언'] = champion_name
                # 6번의 span태그의 text : 챔피언 게임 수, 챔피언 승률, 챔피언 KDA
                champion_info = enemy_info[6].find_element_by_tag_name('span').text.replace(champion_name + ' ', '')
                # 챔피언 게임 수
                champion_played = champion_info[:champion_info.find(' ')]
                # 만약 언랭이면 소환사 정보가 없기 때문에 다음 코드를 실행하지 않는다.
                if champion_played != '':
                    # print(champion_played, end=' / ')
                    summoner_info['판 수'] = champion_played
                    # 챔피언 승률 + KDA
                    while(True):
                        try:
                            win_rate_n_kda = enemy_info[6].find_element_by_tag_name('span').find_elements_by_tag_name('span')
                            break
                        except StaleElementReferenceException:
                            print('StaleElement에러')
                            continue
                    # 챔피언 승률
                    champion_win_rate = win_rate_n_kda[1].text.strip().replace('%', '')
                    # print(champion_win_rate, end=' / ')
                    summoner_info['승률'] = champion_win_rate
                    # 챔피언 KDA
                    champion_kda = win_rate_n_kda[0].text.strip()
                    # print(champion_kda)
                    summoner_info['KDA'] = champion_kda
                else:
                    # champion_played = 'Unrank'
                    summoner_info['판 수'] = 'Unrank'
                    # champion_win_rate = 'Unrank'
                    summoner_info['승률'] = 'Unrank'
                    # champion_kda = 'Unrank'
                    summoner_info['KDA'] = 'Unrank'
                    # print('Unrank')
                enemies_Players_Info[summoner_name] = summoner_info
            team_Players_Info['Enemy'] = enemies_Players_Info
        return team_Players_Info
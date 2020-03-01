from OPGG_ban_champion_getter import OPGG_ban_champion_getter_class
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class Get_Info_Of_All_Summoners_class():
    def Get_Info_Of_All_Summoners_From_Fow(driver, name, team_color):
        url = 'http://fow.kr/find/' + name
        Team_Players_Info = dict()
        driver.get(url)
        driver.implicitly_wait(10)
        while (True):
            try:
                driver.find_element_by_xpath('//a[@tipsy="진행중인 게임에 대한 정보를 볼 수 있습니다."]/span/b').click()
                driver.implicitly_wait(10)
                buffer = driver.find_element_by_xpath('//div[@class="specinfo"]/div').text
                driver.implicitly_wait(10)
                if buffer == '': continue
                else: break
            except NoSuchElementException:
                continue
        # 게임 중이 아님
        if buffer.find('관전하기') == -1:
            print(buffer)
            return None
        # 게임 중임
        else:
            team_info_path = ''
            if team_color == 'blue':
                team_info_path = '//td[@style="background-color:#DDF;"]/div'
            elif team_color == 'red':
                team_info_path = '//td[@style="background-color:#EDF;"]/div'
            # 팀 소환사 5명의 정보가 있는 부분
            Team = driver.find_elements_by_xpath(team_info_path)
            for i in range(0, 5):
                summoner_info = dict()
                # 블루팀 소환사의 정보 7개
                Team_info = Team[i].find_elements_by_tag_name('div')
                # 6번의 b태그의 text : 소환사 이름
                summoner_name = Team_info[6].find_element_by_tag_name('b').text
                # print(summoner_name, end=' / ')
                # 2번의 tipsy : 챔피언 이름
                champion_name = Team_info[1].get_attribute('tipsy')
                # print(champion_name, end=' / ')
                summoner_info['챔피언'] = champion_name
                # 6번의 span태그의 text : 챔피언 게임 수, 챔피언 승률, 챔피언 KDA
                champion_info = Team_info[6].find_element_by_tag_name('span').text.replace(champion_name + ' ', '')
                # 챔피언 게임 수
                champion_played = champion_info[:champion_info.find(' ')]
                # 만약 언랭이면 소환사 정보가 없기 때문에 다음 코드를 실행하지 않는다.
                if champion_played != '':
                    # print(champion_played, end=' / ')
                    summoner_info['판 수'] = champion_played
                    while(True):
                        try:
                            # 챔피언 승률 + KDA
                            win_rate_n_kda = Team_info[6].find_element_by_tag_name('span').find_elements_by_tag_name('span')
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
                # 소환사 정보를 해당 소환사 이름 딕셔너리에 추가한다.
                Team_Players_Info[summoner_name] = summoner_info

            # FOW 밴 정보를 찾음
            ban_infos = driver.find_elements_by_xpath('//div[@class="specinfo"]/div')[2].find_elements_by_tag_name('td')

            team_ban_info_fow = []

            if team_color == 'blue':
                # 블루팀 FOW 밴 정보
                for link in ban_infos[0].find_elements_by_tag_name('img'):
                    team_ban_info_fow.append(str(link.get_attribute('src')))
            elif team_color == 'red':
                # 레드팀 FOW 밴 정보
                for link in ban_infos[2].find_elements_by_tag_name('img'):
                    team_ban_info_fow.append(str(link.get_attribute('src')))

            # 팀 OPGG 밴 정보 리스트
            team_summoner_info_list_opgg = OPGG_ban_champion_getter_class.OPGG_ban_champion_getter_method(driver, name, team_color)
            # 팀 정보 병합
            OPGG_ban_champion_getter_class.OPGG_FOW_info_merger(team_summoner_info_list_opgg, team_ban_info_fow)
            # 최종 딕셔너리에 정보 추가
            for summoner in Team_Players_Info.keys():
                for opgg_info in team_summoner_info_list_opgg:
                    if summoner == opgg_info['이름']:
                        Team_Players_Info[summoner]['티어'] = opgg_info['티어']
                        Team_Players_Info[summoner]['밴'] = opgg_info['밴']
                        Team_Players_Info[summoner]['픽'] = opgg_info['픽']
                        break

        return Team_Players_Info
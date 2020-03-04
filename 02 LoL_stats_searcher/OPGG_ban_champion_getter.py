from selenium.common.exceptions import NoSuchElementException

class OPGG_ban_champion_getter_class():

    def __init__(self):
        pass

    def OPGG_FOW_info_merger(opgg_team_info, fow_ban_info):

        for opgg_ban in opgg_team_info:
            # 밴 챔피언 정보가 없을 때
            if opgg_ban['포우 챔프 링크'] == 'X':
                opgg_ban['밴'] = 'X'
                opgg_ban['픽'] = '모름'
                continue
            # 밴 챔피언 정보가 있을 때
            else:
                cnt = 1
                # FOW 정보에서 차례대로 밴 챔피언 링크를 가져온다
                for fow_ban in fow_ban_info:
                    # 밴된 챔피언을 찾음
                    if fow_ban == opgg_ban['포우 챔프 링크']:
                        opgg_ban['밴'] = opgg_ban['밴']
                        opgg_ban['픽'] = cnt
                        break
                    # 못찾음
                    else:
                        cnt += 1

    def FOW_champ_link_getter(driver, summoner_info_list):
        for info in summoner_info_list:
            summoner_champ = info['밴']
            if summoner_champ != 'X':
                driver.get('http://fow.kr/champs')
                champ_list = driver.find_elements_by_xpath('//div[@class="champ_list"]/ul/a')
                for champ in champ_list:
                    link = str(champ.get_attribute('href'))
                    champ_name = link[link.rfind('/') + 1:]
                    if champ_name == summoner_champ:
                        champ_img_link = str(champ.find_element_by_tag_name('img').get_attribute('src')).replace('_64',
                                                                                                                 '')
                        info['포우 챔프 링크'] = champ_img_link
            else:
                info['포우 챔프 링크'] = 'X'

    def OPGG_team_info_getter(driver, team_color):
        team_info_path = ''
        if team_color == 'blue':
            team_info_path = '//table[@class="Table Team-100"]/tbody/tr'
        elif team_color == 'red':
            team_info_path = '//table[@class="Table Team-200"]/tbody/tr'
        else:
            print("올바른 값이 아닙니다.")
            return None

        # 밴된 챔피언들이 담길 리스트
        banned_champs_list = []
        # 팀 챔피언의 모든 정보가 담길 리스트
        team_summoner_info_list = []
        # 팀 정보
        team_info = driver.find_elements_by_xpath(team_info_path)
        try:
            # 팀 밴 챔피언
            banned_champs = team_info[0].find_element_by_class_name('BannedChampion.Cell').find_elements_by_tag_name(
                'img')
            for bc in banned_champs:
                tmp = str(bc.get_attribute('src'))
                banned_champs_list.append(tmp[tmp.find('champion/') + 9:tmp.rfind('.png')])
        # 총력전 or URF
        except NoSuchElementException:
            pass
        # 팀 소환사 5명의 이름, 티어, 밴 정보를 저장한다
        for i in range(5):
            # 소환사 정보
            summoner_info = team_info[i].find_elements_by_tag_name('td')
            # 소환사의 이름, 티어, 밴등의 정보가 담길 딕셔너리
            summoner_info_dict = dict()
            # 소환사 이름
            summoner_info_dict['이름'] = summoner_info[3].find_element_by_tag_name('a').text
            # 소환사 티어
            summoner_info_dict['티어'] = summoner_info[5].find_element_by_class_name('TierRank').text
            try:
                # 소환사가 밴한 챔피언
                summoner_info_dict['밴'] = banned_champs_list[i]
            except IndexError:
                summoner_info_dict['밴'] = 'X'
            # 저장된 정보들을 리스트에 담는다.
            team_summoner_info_list.append(summoner_info_dict)
        return team_summoner_info_list

    def Get_OPGG_Ingame_driver(driver, name):
        url = 'https://www.op.gg/summoner/userName=' + name
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//dd[@class="Item tabHeader inGame"]/a').click()
        driver.implicitly_wait(10)

    def Get_OPGG_Title(driver, name):
        OPGG_ban_champion_getter_class.Get_OPGG_Ingame_driver(driver, name)
        raw_title = driver.find_element_by_xpath('//div[@class="SpectateSummoner"]/div/div')
        raw_str = raw_title.text
        remove_str = raw_title.find_element_by_tag_name('small').text
        return raw_str[:raw_str.find(remove_str)].strip()

    def OPGG_ban_champion_getter_method(driver, name, team_color):
        OPGG_ban_champion_getter_class.Get_OPGG_Ingame_driver(driver, name)
        team_summoner_info_list = OPGG_ban_champion_getter_class.OPGG_team_info_getter(driver, team_color)
        OPGG_ban_champion_getter_class.FOW_champ_link_getter(driver, team_summoner_info_list)

        # for info in team_summoner_info_list: print(info)
        return team_summoner_info_list
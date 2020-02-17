from selenium.common.exceptions import NoSuchElementException, WebDriverException, UnexpectedAlertPresentException, \
    NoSuchWindowException, ElementClickInterceptedException, ElementNotInteractableException

class Stats_Refresher_class:
    def Fow_Stats_Refresher(summoners_name, driver):
        for name in summoners_name:
            while (True):
                try:
                    # 해당 소환사의 your.gg 페이지를 연다
                    driver.get('http://fow.kr/find/' + name)
                    # 페이지가 열릴 때까지 기다린다
                    driver.implicitly_wait(5)
                    # 전적 갱신 버튼
                    elem = driver.find_element_by_xpath("//div[@class='profile']/div[4]/a/span")
                    if elem.text == '갱신가능':
                        elem.click()
                        print('[FOW]' + name + ' : 갱신완료')
                    elif elem.text == '갱신불가':
                        print('[FOW]' + name + ' : 갱신불가')
                    break
                # driver.find_element_by_xpath에서 발생한 오류(OPGG가 소환사 정보 가져오는게 너무 느려서 발생)
                # -> 소환사 정보페이지 다시 로딩
                except NoSuchElementException:
                    pass
                # driver.get에서 발생한 오류(OPGG가 소환사 정보 가져오는게 너무 느려서 발생)
                # -> 소환사 정보페이지 다시 로딩
                except WebDriverException:
                    pass

    def OPGG_Stats_Refresher(summoners_name, driver):
        for name in summoners_name:
            while (True):
                try:
                    # 해당 소환사의 your.gg 페이지를 연다
                    driver.get('https://www.op.gg/summoner/userName=' + name)
                    # 페이지가 열릴 때까지 기다린다
                    driver.implicitly_wait(5)
                    # 전적 갱신 버튼
                    elem = driver.find_element_by_xpath("//div[@class='Buttons']/button[@id='SummonerRefreshButton']")
                    # 버튼 내용이 '전적 갱신'이면 버튼을 클릭한다.
                    if elem.text == '전적 갱신':
                        elem.click()
                        driver.implicitly_wait(5)
                        print('[OPGG]' + name + ' : 갱신완료')
                    # 아니라면 그 내용을 출력하고 넘어간다.
                    else:
                        print(elem.text)
                    break
                # driver.find_element_by_xpath에서 발생한 오류
                # 몇초 전에 갱신을 했습니다. 몇초 후에 다시 갱신하실 수 있습니다.(OPGG)
                except UnexpectedAlertPresentException:
                    print('[OPGG]' + name + ' : 갱신불가')
                    break
                # driver.find_element_by_xpath에서 발생한 오류(OPGG가 소환사 정보 가져오는게 너무 느려서 발생)
                # -> 소환사 정보페이지 다시 로딩
                except NoSuchElementException:
                    continue
                # driver.get에서 발생한 오류(OPGG가 소환사 정보 가져오는게 너무 느려서 발생)
                # -> 소환사 정보페이지 다시 로딩
                except NoSuchWindowException:
                    continue
                # driver.get에서 발생한 오류(OPGG가 소환사 정보 가져오는게 너무 느려서 발생)
                # -> 소환사 정보페이지 다시 로딩
                except WebDriverException:
                    continue
                except ElementClickInterceptedException:
                    continue

    def YOURGG_Stats_Refresher(summoners_name, driver):
        for name in summoners_name:
            while (True):
                try:
                    # 페이지를 로딩함
                    driver.get('https://your.gg/kr/profile/' + name)
                    # 페이지가 로딩될 때까지 기다림
                    driver.implicitly_wait(10)
                    # 업데이트 여부 확인
                    update_check = driver.find_element_by_xpath('//div[@class="px-3 d-flex flex-column"]/div[3]').text
                    if update_check == '방금':
                        print('[YOURGG]' + name + ': 갱신완료')
                        break
                    # 업데이트 버튼 클릭
                    driver.find_element_by_xpath('//i[@id="profileUpdateRefreshImg"]/..').click()
                # 업데이트 버튼 불가 시 -> 다시시도
                except ElementClickInterceptedException:
                    print('[YOURGG]' + name + ': 갱신불가')
                    break
                # 일시적으로 라이엇 데이터 사용량을 초과하여 서비스 할 수 없습니다. -> 갱신불가
                except UnexpectedAlertPresentException:
                    continue
                except ElementNotInteractableException:
                    continue
                except WebDriverException:
                    continue
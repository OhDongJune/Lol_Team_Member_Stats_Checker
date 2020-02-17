from selenium.common.exceptions import UnexpectedAlertPresentException, ElementClickInterceptedException, \
    ElementNotInteractableException, WebDriverException, NoSuchElementException
import time

class Team_members_stats_checker_class:
    def last10_days_stats(summoners_name, driver):
        se = dict() # 소환사들의 솔로랭크 최근 10게임의 평가정보들이 담길 딕셔너리
        for name in summoners_name:
            # 임시 변수 초기화
            attribute = ''
            score = dict()
            last_match_date = ''
            while (True):
                try:
                    # 메인페이지를 로딩함
                    driver.get('https://your.gg/kr/profile/' + name)
                    # 페이지가 로딩될 때까지 기다림
                    driver.implicitly_wait(10)
                    # 메인페이지의 솔로랭크 탭을 염
                    driver.find_element_by_xpath("//li[@class='nav-item bg-white']/a[@href='#matchSoloRank']").click()
                    # 페이지가 로딩될 때까지 기다림
                    time.sleep(1)
                    try:
                        # 소환사의 제일 최근 솔로랭크 경기일을 가져온다
                        last_match_date = driver.find_element_by_xpath(
                            '//div[@id="matchListSoloRankArea"]/div/div/div/div/span').text
                    # 경기기록이 없을 때
                    except NoSuchElementException:
                        last_match_date = '없음'
                    # 소환사의 평가정보를 가져옴
                    elem = driver.find_elements_by_tag_name('tspan')
                    # 해당 소환사의 평가정보 처리한다.
                    for i in range(10, 20):
                        # 반복인자가 짝수면 항목(attribute)이름을 저장
                        if i % 2 == 0:
                            attribute = str(elem[i].text)
                        # 반복인자가 홀수면 값(value)을 항목을 key로 가지는 임시 딕셔너리 score어에 저장
                        else:
                            score[attribute] = elem[i].text
                    # 딕셔너리에 최근 경기일을 입력한다.
                    score['최근 경기일'] = last_match_date
                    break
                # 일시적으로 라이엇 데이터 사용량을 초과하여 서비스 할 수 없습니다. -> 다시시도
                except UnexpectedAlertPresentException:
                    continue
                except IndexError:
                    continue
            se[name] = score
        # 정보 출력
        print("==솔로랭크 최근 10게임 평가정보==")
        for name in se.keys():
            print(name + ": ", end='')
            print(se[name])
        print('')

    def total_stats(summoners_name, driver):
        se = dict() # 소환사들의 솔로랭크 모든 게임의 평가정보들이 담길 딕셔너리
        for name in summoners_name:
            # 임시 변수 초기화
            attribute = ''
            score = dict()
            while (True):
                try:
                    # 페이지를 로딩함
                    driver.get('https://your.gg/kr/profile/' + name + '/stats')
                    # 페이지가 로딩될 때까지 기다림
                    driver.implicitly_wait(10)
                    # 소환사의 평가정보를 가져옴
                    elem = driver.find_elements_by_tag_name('tspan')
                    # 해당 소환사의 평가정보 처리한다.
                    for i in range(0, len(elem)):
                        # 반복인자가 짝수면 항목(attribute)이름을 저장
                        if i % 2 == 0:
                            attribute = str(elem[i].text)
                        # 반복인자가 홀수면 값(value)을 항목을 key로 가지는 임시 딕셔너리 score어에 저장
                        else:
                            score[attribute] = elem[i].text
                    break
                # 일시적으로 라이엇 데이터 사용량을 초과하여 서비스 할 수 없습니다. -> 다시시도
                except UnexpectedAlertPresentException:
                    continue
                except IndexError:
                    continue
            # score를 se 딕셔너리에 옮겨 담는다.
            se[name] = score
        print("==솔로랭크 모든 게임의 평가정보==")
        # 정보 출력
        for name in se.keys():
            print(name + ": ", end='')
            print(se[name])
        print('')
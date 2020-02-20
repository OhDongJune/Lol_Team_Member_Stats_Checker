from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Get_Names_Of_All_Summoners_class:
    def Get_Names_Of_All_Summoners_From_Fow(driver, name):
        url = 'http://fow.kr/find/' + name
        all_Players = []
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
        if buffer.find('솔로랭크') == -1:
            all_Players.append(buffer)
        # 게임 중임
        else:
            friendlys = driver.find_elements_by_class_name('spec_list_name.nanum')
            for i in range(10):
                all_Players.append(friendlys[i].text)

        return all_Players
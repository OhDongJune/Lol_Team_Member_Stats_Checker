from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException

class Get_driver_class():
    def Get_driver_method(flag):
        # 내 설정을 로드함
        profile = webdriver.FirefoxProfile(
            r'C:\Users\오동준\AppData\Roaming\Mozilla\Firefox\Profiles\rtgnx63y.default-release-1580514955926')
        # headless 옵션으로 webdriver 선언
        if flag == 1:
            op = webdriver.FirefoxOptions()
            op.add_argument('--headless')
            driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe', firefox_options=op, firefox_profile=profile)
        # 일반 webdriver 호출
        elif flag == 0:
            driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe', firefox_profile=profile)
        driver.install_addon(r"C:\adguardadblocker@adguard.com.xpi", temporary=True)
        driver.maximize_window()
        return driver

    def Close_driver(driver):
        while(True):
            try:
                driver.close()
                break
            except UnexpectedAlertPresentException:
                try:
                    driver.switch_to.alert.accept()
                except NoAlertPresentException:
                    break
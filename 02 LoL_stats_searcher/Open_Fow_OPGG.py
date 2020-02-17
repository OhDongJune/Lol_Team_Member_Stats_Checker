import time
import os
import webbrowser

class Open_Fow_OPGG_class:
    def Open_Fow_OPGG_method(summoners_name):
        opgg_url = 'https://www.op.gg/multi/query='
        fow_url = 'http://fow.kr/multi#'

        for name in summoners_name:
            opgg_url += '%2C' + name
            fow_url += name + ','

        # firefox가 켜졌나 안켜졌나 확인
        result = os.system('tasklist | findstr firefox > null')

        # 1이면 안켜짐, 0이면 켜짐
        if result == 0:    os.system("taskkill /im firefox.exe /f > null")
        time.sleep(5)

        # firefox를 webbrowser의 기본 브라우저로 설정
        firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path), 1)

        # opgg,fow 멀티서치 열기
        webbrowser.get('firefox').open(opgg_url)
        time.sleep(2)
        webbrowser.get('firefox').open(fow_url)
        time.sleep(2)
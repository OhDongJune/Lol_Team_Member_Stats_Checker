import time
import webbrowser

class Open_Fow_OPGG_class:
    def Open_Fow_OPGG_method(summoners_name, flag):
        opgg_url = 'https://www.op.gg/multi/query='
        fow_url = 'http://fow.kr/multi#'

        for name in summoners_name:
            opgg_url += '%2C' + name
            fow_url += name + ','

        # firefox를 webbrowser의 기본 브라우저로 설정
        firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path), 1)

        if flag == 1:
            webbrowser.get('firefox').open(opgg_url)
        elif flag == 2:
            webbrowser.get('firefox').open(fow_url)

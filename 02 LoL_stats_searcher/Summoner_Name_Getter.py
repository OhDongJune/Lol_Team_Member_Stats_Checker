import sys

class name_getter:
    # 소환사들의 이름 추출
    def name_extractor(self):

        names = ''
        print('After input the summoners name, type enter twice')
        print('Copy and paste summoners from the chat : ', end='', flush=True)
        while True:
            names += sys.stdin.read(1)
            if (names[-1:] == '\n') & (names[-2:-1] == '\n'):
                break

        name_list = names.split('\n')
        name_list.pop()
        name_list.pop()

        for x in range(0, len(name_list)):
            name_list[x] = name_list[x][:name_list[x].rfind('님')]

        try:
            name_list.remove('...')
        finally:
            # print(li)
            return name_list

    # 소환사 모두 로딩안됐을 때 소환사 추가
    def name_adder(sn):
        new_name = input('If there\'s a summoner\'s name omitted from the chat, \
type the summoner\'s name, \nif there isn\'t , just press enter : ')
        if new_name != '':
            sn.append(new_name)

"""
미래의시대님이 로비에 참가하셨습니다.
아무나이겨라님이 로비에 참가하셨습니다.
지고싶음님이 로비에 참가하셨습니다.
타 잔님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.

JustLikeThatKR님이 로비에 참가하셨습니다.
쟈 칼님이 로비에 참가하셨습니다.
혭나니님이 로비에 참가하셨습니다.
가루눈 OwO님이 로비에 참가하셨습니다.
어디냐님이 로비에 참가하셨습니다.

Anhi님이 로비에 참가하셨습니다.
디스이즈나인님이 로비에 참가하셨습니다.
카드막힌체리님이 로비에 참가하셨습니다.
스마트폰노예님이 로비에 참가하셨습니다.
나루토분신술님이 로비에 참가하셨습니다.

노뮤뮤님이 로비에 참가하셨습니다.
리얼네오님이 로비에 참가하셨습니다.
맥주먹고음주 롤님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.
리오레대윤님이 로비에 참가하셨습니다.

장기판님이 로비에 참가하셨습니다.
좋은감자만나님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.
엠에스의드래곤볼님이 로비에 참가하셨습니다.
김프로k님이 로비에 참가하셨습니다.

그날엔불닭면님이 로비에 참가하셨습니다.
작전명 야필패님이 로비에 참가하셨습니다.
쌀훈아 정거같아님이 로비에 참가하셨습니다.
혀누기다님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.

샴쌍둥이님이 로비에 참가하셨습니다.
이문동학점킬러님이 로비에 참가하셨습니다.
신사멋쟁이님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.
에어파티님이 로비에 참가하셨습니다.

Blood bone님이 로비에 참가하셨습니다.
껌온링링님이 로비에 참가하셨습니다.
왓썹링링님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.
standard9님이 로비에 참가하셨습니다.

남탓장인 노팬티님이 로비에 참가하셨습니다.
허지훈주인님님이 로비에 참가하셨습니다.
밀어라 님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.
잦지용님이 로비에 참가하셨습니다.

조치원주민님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.
YapCHA님이 로비에 참가하셨습니다.
씨엘로이마르님이 로비에 참가하셨습니다.
슈터앤클맨님이 로비에 참가하셨습니다.

백혜인님이 로비에 참가하셨습니다.
사랑할수록님이 로비에 참가하셨습니다.
...님이 로비에 참가하셨습니다.
박 서 0님이 로비에 참가하셨습니다.
치즈닭꼬치님이 로비에 참가하셨습니다.

"""
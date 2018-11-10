# coding=utf8
# !/usr/bin/env python
# note 리눅스 쉘 실행시 인코딩 에러가 나면 위 문구 필요
################################################################################

import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.append(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__))))  # note 다른 경로 파일을 import 할때

################################################################################

IMPLICITLY_WAIT = 100
TIMEOUT = 1


def main(*args, **kwargs):
    try:

        # note linunx 에서는 --headless 외에 아래 옵션을 모두 추가해주어야함, 그리고 chromedriver 뿐만 아니라 리눅스용 크롬 브라우저도 필요함
        # note linux 백그라운드 실행 명령어 "nohup python lyrics.py &" 이렇게 하면 원격에서도 로그아웃하고 데이터를 실행할수 있다.
        # note https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_nohup_%EC%82%AC%EC%9A%A9%EB%B2%95
        # nohup사용법
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--disable-extensions')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--no-sandbox')

        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",
                                  chrome_options=chrome_options)
        driver.set_window_size(1200, 1000)
        # 수집해야할 URL 수집

        driver.get("http://www.naver.com")
        driver.implicitly_wait(IMPLICITLY_WAIT)
        time.sleep(TIMEOUT)
        # 로그인
        driver.execute_script("""
        
        """)


    except Exception as e:
        print('에러 : {error}'.format(error=e))
    finally:
        if driver is not None:
            driver.quit()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

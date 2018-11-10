#!/usr/bin/env python
# note 리눅스 쉘 실행시 인코딩 에러가 나면 위 문구 필요
################################################################################

import os
import sys

sys.path.append(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__))))  # note 다른 경로 파일을 import 할때

################################################################################


def main(*args, **kwargs):
    try:
        for arg in args:
            print("argument : ", arg)

    except Exception as e:
        print('에러 : {error}'.format(error=e))
    finally:
        print('프로그램 종료')


if __name__ == "__main__":
    main(*sys.argv[1:])

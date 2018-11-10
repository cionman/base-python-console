import json
import os


def get_secret(setting):
    """
    파일로 분리된 개인정보를 얻어오는 함수
    :param setting:
    :return:
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    secret_file = os.path.join(BASE_DIR,
                               'key.json')  # secrets.json 파일 위치를 명시

    with open(secret_file) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[setting]
    except KeyError:
        print("secret 정보 확인 중 에러")

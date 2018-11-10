import os

import pymysql
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.util import get_secret


class DatabaseManager:
    """
    클래스 주석
    """
    DB_HOST = get_secret("DB_HOST")
    DB_LOGIN_ID = get_secret("DB_LOGIN_ID")
    DB_PASSWORD = get_secret("DB_PASSWORD")
    DB_NAME = get_secret("DB_NAME")
    DB_PORT = int(get_secret("DB_PORT"))

    def __init__(self):
        self.conn = pymysql.connect(host=self.DB_HOST, port=self.DB_PORT,
                                    user=self.DB_LOGIN_ID,
                                    password=self.DB_PASSWORD,
                                    db=self.DB_NAME, charset='utf8mb4',
                                    autocommit=True)

    def close(self):
        if self.conn:
            self.conn.close()

    def is_collect(self, url) -> bool:  # note 함수 타입 힌트 기능
        """
        수집된적 있는지 확인하여 수집된적 없으면 True
        :param url:
        :return:
        """
        result = False
        try:
            cursor = self.conn.cursor()
            sql = "SELECT ch_id FROM Crawl_History WHERE ch_url = %s"
            cursor.execute(sql, (url,))
            result = cursor.rowcount == 0  # 수집된적이 없으면 true
        except Exception as e:
            self.error_print(e)
        finally:
            if cursor:
                cursor.close()
            return result

    def get_user(self):  # note 함수 타입 힌트 기능

        result = None
        try:
            cursor = self.conn.cursor()
            sql = "SELECT USER_SEQNO, USER_NAME FROM USER"
            cursor.execute(sql)
            result = cursor.fetchall()  # 수집된적이 없으면 true
        except Exception as e:
            self.error_print(e)
        finally:
            if cursor:
                cursor.close()
            return result

    def insert_collect_url(self, url):
        """
        수집할 url 테이블(Crawl_Collect_url)에 insert
        :param url:
        :return:
        """
        try:
            cursor = self.conn.cursor()
            sql = """
                            INSERT INTO Crawl_Collect_Url 
                                (ccu_url, ccu_idate)
                            VALUES
                                (%(url)s, NOW()) 
                        """
            cursor.execute(sql, {'url': url})
        except Exception as e:
            self.error_print(e)
        finally:
            if cursor:
                cursor.close()

    def insert_content_data(self, insert_id, cate_id, title, content,
                            cate_text):
        """
        일반적인 제목과 컨텐츠로 이루어진 데이터를 수집하는 테이블(Crawl_Content_Data) insert
        :param insert_id: history id
        :param cate_id: 카테고리 id
        :param title: 제목
        :param content: 내용
        :param cate_text: 네이버 카테고리 명칭
        :return:
        """
        try:
            if insert_id > 0 and content:
                cursor = self.conn.cursor()
                sql = """
                    INSERT INTO Crawl_Content_Data
                        (ccd_history_id, ccd_categry_id, ccd_title, ccd_content, ccd_idate, ccd_naver_cate)
                    VALUES
                        (%(history_id)s, %(category_id)s, %(title)s, %(content)s,NOW(), %(cate)s)
                """
                cursor.execute(sql, {'history_id': insert_id,
                                     'category_id': cate_id, 'title': title,
                                     'content': content, 'cate': cate_text})
        except Exception as e:
            self.error_print(e)
        finally:
            if cursor:
                cursor.close()

    def insert_history(self, site_name, url):
        """
        수집 기록 저장
        :param site_name:
        :param url:
        :return:
        """
        result = None
        try:
            cursor = self.conn.cursor()
            sql = """
                    INSERT INTO Crawl_History
                        (ch_site_name, ch_url, ch_idate)
                    VALUES
                        (%(site_name)s, %(url)s, NOW())
                                                    """
            cursor.execute(sql, {'site_name': site_name,
                                 'url': url})
            result = cursor.lastrowid
        except Exception as e:
            self.error_print(e)
        finally:
            if cursor:
                cursor.close()
            return result

    def error_print(self, error):
        """
        error 출력
        :param error:
        :return:
        """
        print('''
        에러 : {class_name}.{method_name}
        에러메세지 : {error}
        '''.format(
            class_name=self.__class__.__name__
            , method_name=sys._getframe(1).f_code.co_name, error=error)
        )

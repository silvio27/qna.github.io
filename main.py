#!/usr/bin/python3
# -*- coding: gbk -*-
# @Time    : 2021/6/11 17:03
# @Author  : Silvio27
# @Email   : silviosun@outlook.com
# @File    : main.py
# @Software: PyCharm

import json
import uuid
import pymysql
import datetime


def addtodata():
    datatotal = {
        'id': '',  # * ����id [�Զ�����]
        'title': '',  # * ����
        'describe': '',  # ��Ҫ����
        'content': [],  # ��������,�Ű�������ν��?���Ƽ���ͼ?���item������,����Ƕ��markdown?
        'ref': '',  # ������Դ
        'create_time': '',  # * ����ʱ��
        'update_time': '',  # * ���´���ӵ�ʱ��
        'comments': [],  # comment ������Ӻܶ�comment[id] = data,���Ｔ˼���Ƿ����⼴��?
        'tags': [],  # push tag_id
        'isTodo': False,  # ѡ���Ƿ���һ����������?checkbox Ĭ��false
        'status': False,  # �Ƿ������ [���ش�,�ѹر�??# ] Ĭ��false
        'created_by_id': [],  # �Զ���Ӹ��׼�id,�ɺζ���,�����ж����Ŀ���ϴ������Ŀ,����ѡ,ѡ����Ӵ�
        # 'create_person': '',  # *˭����
        # 'managers': [],  # ˭����
        # 'operators': [],  # ˭ִ��
        # 'inspectors': [],  # ˭�鿴
        'isShow': True,  # �Ƿ���ʾ tinyint(1)
        # 'isAlert': False,  # �Ƿ�Ҫ�����ѹ���?
        # 'alertTime': '',  # ����ʱ�� ˼�����ѵķ�ʽ,ֱ����ҳ����?
    }
    tags = {
        'id': 0,
        'title': '',
        'isUsed': True
    }

    data = {
        'id': '',  # * ����id [�Զ�����]
        'title': '',  # * ����
        'comments': [],  # comment ������Ӻܶ�comment[id] = data,���Ｔ˼���Ƿ����⼴��?
        'tags': [],  # push tag_id tag����tag��,����id�����
        'update_time': '',  # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
    datum = []

# �ֵ� to Json
def dict2json(datum):
    return json.dumps(datum, ensure_ascii=False)

# д���ļ�
def write_to_file(sth, filename='datalist.json'):
    with open(filename, 'w') as f:
        f.write(sth)

    print('Done')

# �������ݿ�
def connect_db(sql):
    cnx = pymysql.connect(
        user='root',
        password='Mysql9127Fir',
        host='localhost',
        database='MyPage'
    )
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
    except:
        print(sql)

    cnx.commit()
    asw = cursor.fetchall()
    cursor.close()
    cnx.close()
    return asw

    newTable = """
        CREATE TABLE sh_db(
        id INT UNSIGNED AUTO_INCREMENT,
        rpid VARCHAR(16) NOT NULL,
        Title VARCHAR(50) NOT NULL,
        CreatTime DATE,
        ReplayTime DATE,
        Content TEXT,
        Reply TEXT,
        Dept VARCHAR(30),
        PRIMARY KEY(id)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;

        """

    check_db = 'select * from sh_db'

# ���������嵥�ʹ��嵥
def update_qna_list():
    tags = {
        1: "questionlist.json",
        2: "answerlist.json"
    }

    def get_list(tablename, tag=1):
        sql = f"select * from {tablename}"
        dict = {}
        for i in connect_db(sql):
            if tag in eval(i[8]):
                dict[i[0]] = {
                    "title": i[1],
                    "describe": i[2],
                    "content": i[3],
                    "ref": i[4],
                    "create_time": str(i[5]),
                    "update_time": str(i[6]),
                    "comments": eval(i[7]) if i[7] else i[7],
                    "tags": eval(i[8]),
                    "created_by": i[9],
                    "isShow": i[10]
                }
        return dict2json(dict)

    for (tag, filename) in tags.items():
        write_to_file(get_list(tablename='qnalist', tag=tag), filename=filename)


if __name__ == '__main__':
    data = {
        '1': {
            'title': '�ҵĵ�һ������?',
            'comments': [2, 3],
            'tags': [1],
            'update_time': '2021-06-11 13:06:08',

        },
        '2': {
            'title': '�ҵĵ�һ���ش�',
            'comments': [],
            'tags': [2],
            'update_time': '2021-06-12 21:06:08',

        },
        '3': {
            'title': '�ҵĵ�2������?',
            'comments': [],
            'tags': [1],
            'update_time': '2021-06-12 23:06:08',

        },
        '4': {
            'title': '�ҵĵڶ�������',
            'comments': [3],
            'tags': [1, 2],
            'update_time': '2021-06-13 00:31:08',

        }
    }

    update_qna_list()

    # jsdata = dict2json(data)
    # write_to_file(jsdata)
    # print(jsdata)

    # sql_desc = "desc qnalist"
    # sqldata = connect_db(sql)
    # for i in sqldata:
    #     print(i[0], end=',\t')
    # print()

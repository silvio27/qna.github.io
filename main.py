#!/usr/bin/python3
# -*- coding: gbk -*-
# @Time    : 2021/6/11 17:03
# @Author  : Silvio27
# @Email   : silviosun@outlook.com
# @File    : main.py
# @Software: PyCharm

import json
import uuid


def addtodata():
    datatotal = {
        'id': '',  # * ����id [�Զ�����]
        'title': '',  # * ����
        'describe': '',  # ��Ҫ����
        'content': {
            'text': '',
            'pic': {
                'title': '',
                'describe': '',
                'urls': []  # �������ͼƬ�����ֲ�
            }
        },  # ��������,�Ű�������ν��?���Ƽ���ͼ?
        'ref': '',  # ������Դ
        'create_time': '',  # * ����ʱ��
        'update_time': '',  # * ���´���ӵ�ʱ��
        'comments': [],  # comment ������Ӻܶ�comment[id] = data,���Ｔ˼���Ƿ����⼴��?
        'tags': [],  # push tag_id
        'isTodo': False,  # ѡ���Ƿ���һ����������?checkbox Ĭ��false
        'status': False,  # �Ƿ������ [���ش�,�ѹر�??# ] Ĭ��false
        'created_by_id': [],  # �Զ���Ӹ��׼�id,�ɺζ���,�����ж����Ŀ���ϴ������Ŀ,����ѡ,ѡ����Ӵ�
        'create_person': '',  # *˭����
        'managers': [],  # ˭����
        'operators': [],  # ˭ִ��
        'inspectors': [],  # ˭�鿴
        'isShow': True,  # �Ƿ���ʾ
        'isAlert': False,  # �Ƿ�Ҫ�����ѹ���?
        'alertTime': '',  # ����ʱ�� ˼�����ѵķ�ʽ,ֱ����ҳ����?
    }

    data = {
        'id': '',  # * ����id [�Զ�����]
        'title': '',  # * ����
        'comments': [],  # comment ������Ӻܶ�comment[id] = data,���Ｔ˼���Ƿ����⼴��?
        'tags': [],  # push tag_id tag����tag��,����id�����
        'update_time': '',  # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
    datum = []


def dict2json(datum):
    return json.dumps(datum, ensure_ascii=False)


def write_to_file(sth, filename='datalist.json'):
    with open(filename, 'w') as f:
        f.write(sth)


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
    jsdata = dict2json(data)
    write_to_file(jsdata)
    print(jsdata)

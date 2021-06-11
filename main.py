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
    }
    datum = []


def dict2json(datum):
    return json.dumps(datum, ensure_ascii=False)


if __name__ == '__main__':
    data = {
        '1': {
            'title': '�ҵĵ�һ������?',
            'comments': [2,3],
            'tags': [],

        },
        '2': {
            'title': '�ҵĵ�һ���ش�',
            'comments': [],
            'tags': [],

        },
        '3': {
            'title': '�ҵĵ�2������?',
            'comments': [],
            'tags': [],

        }
    }
    print(dict2json(data))

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
        'id': '',  # * 问题id [自动生成]
        'title': '',  # * 名称
        'describe': '',  # 简要描述
        'content': [],  # 完整内容,排版问题如何解决?类似见下图?多个item做换行,后期嵌入markdown?
        'ref': '',  # 问题来源
        'create_time': '',  # * 创建时间
        'update_time': '',  # * 最新答案添加的时间
        'comments': [],  # comment 可以添加很多comment[id] = data,这里即思考是否问题即答案?
        'tags': [],  # push tag_id
        'isTodo': False,  # 选择是否是一个代办事项?checkbox 默认false
        'status': False,  # 是否已完成 [待回答,已关闭??# ] 默认false
        'created_by_id': [],  # 自动添加父亲级id,由何而来,可能有多个题目联合创造的题目,即多选,选择添加答案
        # 'create_person': '',  # *谁创建
        # 'managers': [],  # 谁负责
        # 'operators': [],  # 谁执行
        # 'inspectors': [],  # 谁查看
        'isShow': True,  # 是否显示 tinyint(1)
        # 'isAlert': False,  # 是否要有提醒功能?
        # 'alertTime': '',  # 提醒时间 思考提醒的方式,直接网页弹出?
    }
    tags = {
        'id': 0,
        'title': '',
        'isUsed': True
    }

    data = {
        'id': '',  # * 问题id [自动生成]
        'title': '',  # * 名称
        'comments': [],  # comment 可以添加很多comment[id] = data,这里即思考是否问题即答案?
        'tags': [],  # push tag_id tag进入tag库,返回id到这边
        'update_time': '',  # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
    datum = []


def dict2json(datum):
    return json.dumps(datum, ensure_ascii=False)


def write_to_file(sth, filename='datalist.json'):
    with open(filename, 'w') as f:
        f.write(sth)

    print('Done')


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


if __name__ == '__main__':
    data = {
        '1': {
            'title': '我的第一个问题?',
            'comments': [2, 3],
            'tags': [1],
            'update_time': '2021-06-11 13:06:08',

        },
        '2': {
            'title': '我的第一个回答',
            'comments': [],
            'tags': [2],
            'update_time': '2021-06-12 21:06:08',

        },
        '3': {
            'title': '我的第2个问题?',
            'comments': [],
            'tags': [1],
            'update_time': '2021-06-12 23:06:08',

        },
        '4': {
            'title': '我的第二个问题',
            'comments': [3],
            'tags': [1, 2],
            'update_time': '2021-06-13 00:31:08',

        }
    }
    # jsdata = dict2json(data)
    # write_to_file(jsdata)
    # print(jsdata)
    sql = "desc qnalist"
    sqldata = connect_db(sql)
    for i in sqldata:
        print(i[0], end=',\t')
    print()

    sql = "select * from qnalist"
    sqldata = connect_db(sql)
    for i in sqldata:
        print(i)

    aa = sqldata[0][5]
    print(aa)
    A = {}

    for i in sqldata:
        A[i[0]]={
            "title": i[1],
            "describe":i[2],
            "content":i[3],
            "ref":i[4],
            "create_time":str(i[5]),
            "update_time":str(i[6]),
            "comments":i[7],
            "tags":i[8],
            "created_by":i[9],
            "isShow":i[10]
        }


    ans = dict2json(A)
    write_to_file(ans,'datalistbysql.json')

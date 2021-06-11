#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 17:03
# @Author  : Silvio27
# @Email   : silviosun@outlook.com
# @File    : main.py
# @Software: PyCharm

def addtodata():
    data = {
        'id': '',  # * 问题id [自动生成]
        'title': '',  # * 名称
        'describe': '',  # 简要描述
        'content': {
            'text': '',
            'pic': {
                'title': '',
                'describe': '',
                'urls': []  # 如果多张图片即做轮播
            }
        },  # 完整内容,排版问题如何解决?类似见下图?
        'ref': '',  # 问题来源
        'create_time': '',  # * 创建时间
        'update_time': '',  # * 最新答案添加的时间
        'comments': [],  # comment 可以添加很多comment[id] = data,这里即思考是否问题即答案?
        'tags': [],  # push tag_id
        'isTodo': False,  # 选择是否是一个代办事项?checkbox 默认false
        'status': False,  # 是否已完成 [待回答,已关闭??# ] 默认false
        'created_by_id': [],  # 自动添加父亲级id,由何而来,可能有多个题目联合创造的题目,即多选,选择添加答案
        'create_person': '',  # *谁创建
        'managers': [],  # 谁负责
        'operators': [],  # 谁执行
        'inspectors': [],  # 谁查看
        'isShow': True,  # 是否显示
        'isAlert': False,  # 是否要有提醒功能?
        'alertTime': '',  # 提醒时间 思考提醒的方式,直接网页弹出?
    }


if __name__ == '__main__':
    print('hello')

#!/usr/bin/python3
# -*- coding: gbk -*-
# @Time    : 2021/6/13 16:51
# @Author  : Silvio27
# @Email   : silviosun@outlook.com
# @File    : fastapi_serve.py
# @Software: PyCharm

# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 17:28
# @Author  : Silvio27
# @Email   : silviosun@outlook.com
# @File    : main.py
# @Software: PyCharm
import os, sys
from typing import Optional
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import time
from temp.main import connect_db, update_qna_list
from deal_picture import File_W_R
from starlette.responses import StreamingResponse
from deal_picture import from_raw_to_thumbnail

app = FastAPI()

# 前端页面url
origins = ['*']

# 后台api允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/message")
async def root():
    return {
        "message": "Hello World",
        "name": "Sun",
        "Gender": "male",
        "Age": "20"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# 打开某个文件
@app.get("/file/{s}")
def root(s: str):
    with open(s, 'r') as f:
        aa = f.read()
    return eval(aa)


@app.get("/addanswer/{s}")
def add_answer(s: str):
    print('答案:' + s)
    ans = s.split('+')
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 创建答案
    sql = f'''
                INSERT INTO qnalist 
                (title,create_time,update_time,tags,created_by) VALUES 
                ('{ans[0]}','{now}','{now}', '[2]',{ans[1]})
            '''
    print(connect_db(sql))
    ## 更新问题的答案list
    # 获得答案的id
    sql = f"select id from qnalist where title= '{ans[0]}'"
    an_id = connect_db(sql)[0][0]
    # 获得问题的id
    sql = f'''select comments from qnalist where id= {ans[1]}'''
    jg = connect_db(sql)[0][0]
    # 如果原来的comments为空则创建[],不然就append到[]
    if jg is None:
        lb = [an_id]
    else:
        lb = eval(jg)
        lb.append(an_id)
    # 更新到问题comments中
    sql = f"update qnalist set comments = '{lb}' where id= '{ans[1]}'"
    connect_db(sql)

    # 更新问题和答案列表
    update_qna_list()
    return s


@app.get("/addquestion/{s}")
def add_question(s: str):
    print('问题:' + s)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql = f'''
            INSERT INTO qnalist 
            (title,create_time,update_time,tags) VALUES 
            ('{s}','{now}','{now}', '[1]')
        '''
    connect_db(sql)
    update_qna_list()
    return s


# 返回照片字典key值列表，按升序排序
@app.get("/data/keylist")
def get_raw_data():
    data = File_W_R(base_path='./', filename='dict_data.txt').get_data()
    bkdata = []
    for i in sorted(eval(data)):
        bkdata.append(i)
    return bkdata


# 根据照片id获得照片返回照片所有数据
@app.get("/data/key/{key}")
def get_pic_thumbnail_url(key: int):
    data = File_W_R(base_path='./', filename='dict_data.txt').get_data()
    print(data)
    data = eval(data)[key]
    return data


# TODO 根据图片名称返回图片,目前路径是写死的,后期再优化，
# TODO 如何根据打开的文件夹修改路径，或者在默认路径上？ + 添加默认压缩文件夹名称
@app.get("/image/{name}")
def show_pic(name):
    raw_path = os.getcwd() + '/origin_thumbnail/' + name
    file_like = open(raw_path, mode="rb")
    return StreamingResponse(file_like, media_type="image/jpg")


@app.get("/data/backdata/{id}/{data}")
def get_tags(id: int, data: Optional[str] = None):
    print(id, data)
    res = eval(File_W_R(base_path='./', filename='dict_data.txt').get_data())
    res[id]['sort_tags'] = data
    print('after'+str(res))
    File_W_R(base_path='./', filename='dict_data.txt').write_file(str(res))
    return 'ok'


if __name__ == '__main__':
    uvicorn.run(app='fastapi_serve:app', host="0.0.0.0", port=8888, reload=True, debug=True)

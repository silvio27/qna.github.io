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


from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware.cors import CORSMiddleware
import uvicorn
import time
from main import connect_db, update_qna_list,dict2json

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

@app.get("/message")
async def root():
    return {
        "message": "Hello World",
        "name": "Sun",
        "Gender": "male",
        "Age": "20"
    }


@app.get("/thisisid/{id}")
def read_item(id: int):
    id += 10
    return {"item_id": id}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


from starlette.responses import StreamingResponse
@app.get("/image/1")
def show_pic():
    file_like = open('/Users/silvio/Desktop/IMG_1283.png', mode="rb")
    return StreamingResponse(file_like, media_type="image/png")

@app.get("/image/2")
def show_pic():
    file_like = open('/Users/silvio/Desktop/lifecycle.png', mode="rb")
    return StreamingResponse(file_like, media_type="image/png")


if __name__ == '__main__':
    uvicorn.run(app='fastapi_serve:app', host="0.0.0.0", port=8888, reload=True, debug=True)

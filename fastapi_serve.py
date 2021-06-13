#!/usr/bin/python3
# -*- coding: utf-8 -*-
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
    return s


@app.get("/addquestion/{s}")
def add_question(s: str):
    print('问题:' + s)
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


if __name__ == '__main__':
    uvicorn.run(app='fastapi_serve:app', host="0.0.0.0", port=8888, reload=True, debug=True)

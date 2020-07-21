#!/usr/bin/env python
# -*- conding: utf-8 -*-
# @Author:xxx
# @Time : 2020/7/11 18:29
# @File :conftest.py
# @Software:
from typing import List
import  yaml
import pytest

from pythoncode.calc import Calulator


@pytest.fixture()
def fun_calc():
    cal = Calulator()
    return cal


@pytest.fixture()
def setup_teardown_calc(fun_calc):
    print('计算开始')
    yield fun_calc
    print('计算结束')

# 解决中文乱码
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')



# 通过 方法动态的生成测试用例
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param1" in metafunc.fixturenames:
        metafunc.parametrize("param1",
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function')

def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    with open('data/st/data.yaml') as f:
        datas = yaml.safe_load(f)

        if myenv == 'test':
            data = datas['test']
        elif myenv == 'dev':
            data = datas['dev']
        else:
            data = datas['st']

    return myenv, data
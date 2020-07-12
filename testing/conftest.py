#!/usr/bin/env python
# -*- conding: utf-8 -*-
# @Author:xxx
# @Time : 2020/7/11 18:29
# @File :conftest.py
# @Software:
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

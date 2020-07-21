#!/usr/bin/env python
# -*- conding: utf-8 -*-
# @Author:xxx
# @Time : 2020/7/11 13:57
# @File :test_calc.py
# @Software:

import pytest
import yaml


class TestCalc:
    # # @pytest.mark.parametrize('a,b,result',
    #                          yaml.safe_load(open('data/test/data.yaml')))

    myids=['整数']
    # with open('data/test/data.yaml') as f:
    #     datas=yaml.safe_load(f)
    #
    #     print(datas)
    mydatas =[[1,2,3]]
    @pytest.mark.run(order=1)
    @pytest.mark.dependency()
    def test_add(self, setup_teardown_calc, param1):
        assert param1[2] == setup_teardown_calc.add(param1[0], param1[1])

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['test_ride'])
    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('data/test/data.yaml')))
    def test_div(self, setup_teardown_calc, a, b, result):
        assert result == setup_teardown_calc.div(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['test_add'])
    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('data/test/data.yaml')))
    def test_sub(self, setup_teardown_calc, a, b, result):
        assert result == setup_teardown_calc.sub(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.dependency()
    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('data/test/data.yaml')))
    def test_ride(self, setup_teardown_calc, a, b, result):
        assert result == setup_teardown_calc.ride(a, b)

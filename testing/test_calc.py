#!/usr/bin/env python
# -*- conding: utf-8 -*-
# @Author:xxx
# @Time : 2020/7/11 13:57
# @File :test_calc.py
# @Software:

import pytest
import yaml


class TestCalc:
    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('D:\\Studies\\ceshiren\\HogwartsSdet14\\yamlData/addyaml_1.yaml')))
    def test_add(self, setup_teardown_calc, a, b, result):
        assert result == setup_teardown_calc.add(a, b)

    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('D:\\Studies\\ceshiren\\HogwartsSdet14\\yamlData/addyaml_2.yaml')))
    def test_div(self, setup_teardown_calc, a, b, result):
        assert result == setup_teardown_calc.div(a, b)

    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('D:\\Studies\\ceshiren\\HogwartsSdet14\\yamlData/addyaml_3.yaml')))
    def test_sub(self, setup_teardown_calc, a, b, result):
        assert result == setup_teardown_calc.sub(a, b)

    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('D:\\Studies\\ceshiren\\HogwartsSdet14\\yamlData/addyaml_4.yaml')))
    def test_ride(self, setup_teardown_calc, a, b, result):
        assert result == setup_teardown_calc.ride(a, b)

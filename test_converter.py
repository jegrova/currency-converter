"""
Module for testing
"""

import pytest
from converter import Converter, ConverterError


def test_currency_object_initialization():
    obj = Converter(10, 'CZK', 'EUR')
    assert obj.amount == 10
    assert obj.input_cur == 'CZK'
    assert obj.output_cur == 'EUR'

    cur_obj = Converter(10, 'USD')
    assert cur_obj.amount == 10
    assert cur_obj.input_cur == 'USD'


def test_initialize_list_currencies():
    cur_obj = Converter(10, 'CZK')
    list_cur = cur_obj.initialize_list_currencies()

    list_of_currencies = ['usd', 'eur', 'gbp', 'aud', 'chf', 'cad', 'jpy', 'uyu', 'gyd', 'rwf', 'lsl', 'npr', 'cop', 'php', 'tjs', 'crc',
     'nad', 'sdg', 'ern', 'sos', 'inr', 'bbd', 'twd', 'irr', 'mga', 'xcd', 'ang', 'mop', 'wst', 'myr', 'huf', 'pen',
     'lbp', 'tnd', 'svc', 'awg', 'zmw', 'gtq', 'bam', 'nok', 'hrk', 'bdt', 'gel', 'stn', 'djf', 'all', 'omr', 'bwp',
     'rub', 'hkd', 'kzt', 'pyg', 'fjd', 'cdf', 'szl', 'mvr', 'clp', 'sek', 'mxn', 'tmt', 'bob', 'lrd', 'ssp', 'ngn',
     'kes', 'dkk', 'aed', 'xof', 'uah', 'afn', 'ttd', 'htg', 'top', 'ugx', 'cny', 'kwd', 'bgn', 'pgk', 'iqd', 'mad',
     'etb', 'cve', 'mwk', 'cup', 'vuv', 'nzd', 'isk', 'byn', 'rsd', 'mkd', 'xpf', 'mmk', 'qar', 'sar', 'brl', 'amd',
     'ars', 'bzd', 'kmf', 'sll', 'lkr', 'zar', 'ils', 'mdl', 'ves', 'jmd', 'gip', 'mzn', 'scr', 'thb', 'xaf', 'uzs',
     'nio', 'srd', 'syp', 'mru', 'tzs', 'krw', 'bhd', 'vnd', 'egp', 'pab', 'sbd', 'lak', 'dop', 'mnt', 'mur', 'ron',
     'pkr', 'lyd', 'ghs', 'gmd', 'bif', 'aoa', 'yer', 'dzd', 'pln', 'try', 'azn', 'jod', 'bsd', 'gnf', 'hnl', 'khr',
     'bnd', 'sgd', 'idr', 'kgs']

    assert set(list_cur) == set(list_of_currencies)


def test_create_dict():
    cur_obj = Converter(1, 'USD', 'CZK')
    value = 25
    dictionary = cur_obj.create_dict(value)
    result = {
            'input': {
                'amount': 1,
                'currency': 'USD',
            },
            'output': 25
        }
    assert dictionary == result

    currency_obj = Converter(1, 'CZK')
    value = {
        'USD': 0.044,
        'EUR': 0.039,
        'GBP': 0.035
    }
    dictionary = cur_obj.create_dict(value)
    result = {
        'input': {
            'amount': 1,
            'currency': 'USD',
        },
        'output': {
                     'USD': 0.044,
                     'EUR': 0.039,
                     'GBP': 0.035
                 }
    }

    assert dictionary == result


def test_input_validation_xxx():
    with pytest.raises(ConverterError, match=r"Unknown currency"):
        cur_obj = Converter(1, 'xxx')


def test_input_validation_ambiguous():
    with pytest.raises(ConverterError, match=r"Input currency is ambiguous, did you mean: "):
        cur_obj = Converter(1, '$')


def test_input_validation_unknown():
    with pytest.raises(ConverterError, match=r"Unknown currency"):
        cur_obj = Converter(1, 'yzx')

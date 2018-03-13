import pytest

from ordered_dict import OrderedDict


def test_set_new_items():
    d = OrderedDict()
    assert d.keys() == []
    assert d.values() == []

    d['language'] = 'Python'
    assert d.keys() == ['language']
    assert d.values() == ['Python']

    d['other'] = ('a', 'b', 'c')
    assert d.keys() == ['language', 'other']
    assert d.values() == ['Python', ('a', 'b', 'c')]


def test_items_method():
    d1 = OrderedDict()

    d1['a'] = 1
    d1['b'] = 2
    d1['c'] = 3
    d1['d'] = 4

    assert d1.items() == [
        ('a', 1),
        ('b', 2),
        ('c', 3),
        ('d', 4),
    ]


def test_get_items_with_existent_items():
    d = OrderedDict()

    d['language'] = 'Python'
    d['other'] = ('a', 'b', 'c')
    assert d['language'] == 'Python'
    assert d['other'] == ('a', 'b', 'c')


def test_get_items_with_missing_items():
    d = OrderedDict()

    d['language'] = 'Python'

    assert d['language'] == 'Python'
    with pytest.raises(KeyError):
        d['other-key']


def test_membership():
    d = OrderedDict()

    d['language'] = 'Python'
    d['other'] = ('a', 'b', 'c')
    assert 'language' in d
    assert 'other' in d

    assert 'not-found' not in d


def test_count_items():
    d = OrderedDict()

    assert len(d) == 0

    d['language'] = 'Python'
    assert len(d) == 1

    d['other'] = ('a', 'b', 'c')
    assert len(d) == 2


def test_dictionaries_are_equal():
    d1 = OrderedDict()
    d1['a'] = 1
    d1['b'] = 2

    d2 = OrderedDict()
    d2['a'] = 1
    d2['b'] = 2

    assert d1 == d2


def test_equal_compared_to_python_dict():
    d1 = OrderedDict()
    d1['a'] = 1
    d1['b'] = 2

    assert d1 == {'a': 1, 'b': 2}


def test_dictionaries_are_not_equal_elements():
    d1 = OrderedDict()
    d1['a'] = 1
    d1['b'] = 2

    d2 = OrderedDict()
    d2['c'] = 1
    d2['d'] = 2

    assert d1 != d2


def test_str_and_repr():
    d = OrderedDict()
    assert str(d) == "{}"
    assert repr(d) == str(d)

    d['a'] = 1
    assert str(d) == "{'a': 1}"
    assert repr(d) == str(d)

    d['language'] = 'Python'

    assert str(d) == "{'a': 1, 'language': 'Python'}"
    assert repr(d) == str(d)

    d['points'] = (13, 4)
    assert str(d) == "{'a': 1, 'language': 'Python', 'points': (13, 4)}"
    assert repr(d) == str(d)


def test_add_two_dicts_with_unique_keys():
    d1 = OrderedDict()
    d1['a'] = 1
    d1['b'] = 2

    d2 = OrderedDict()
    d2['c'] = 3
    d2['d'] = 4

    d3 = d1 + d2

    assert d3 == {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }

def test_from_keys_with_sequences():
    d = OrderedDict.from_keys('abc')
    assert d == {
        'a': None,
        'b': None,
        'c': None
    }

    d = OrderedDict.from_keys(['a', 'b', 'c'])
    assert d == {
        'a': None,
        'b': None,
        'c': None
    }

    d = OrderedDict.from_keys(['abc', 'def'])
    assert d == {
        'abc': None,
        'def': None
    }

def test_add_two_dicts_with_repeated_keys():
    d1 = OrderedDict()
    d1['a'] = 1
    d1['b'] = 2

    d2 = OrderedDict()
    d2['c'] = 3
    d2['a'] = 4  # repeated

    d3 = d1 + d2

    assert d3 == {
        'a': 4,  # updated
        'b': 2,
        'c': 3
    }


def test_set_repeated_items():
    d = OrderedDict()
    assert d.keys() == []
    assert d.values() == []

    d['language'] = 'Python'
    assert d.keys() == ['language']
    assert d.values() == ['Python']

    d['other'] = ('a', 'b', 'c')
    assert d.keys() == ['language', 'other']
    assert d.values() == ['Python', ('a', 'b', 'c')]

    # Same key again:
    d['language'] = 'Ruby'
    assert d.keys() == ['language', 'other']
    assert d.values() == ['Ruby', ('a', 'b', 'c')]



def test_dictionaries_are_not_equal_order():
    d1 = OrderedDict()
    d1['a'] = 1
    d1['b'] = 2

    d2 = OrderedDict()
    d2['b'] = 2
    d2['a'] = 1

    assert d1 != d2

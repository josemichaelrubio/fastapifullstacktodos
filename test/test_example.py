# Run: pytest test/test_example.py
# Run all: pytest

def test_equal_or_not_equal():
    assert 1 == 1
    assert 1 != 2

def test_is_instance():
    assert isinstance(1, int)
    assert isinstance(1.0, float)

def test_is_not_instance():
    assert not isinstance(1, float)
    assert not isinstance(1.0, int)

def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'false') is False

def test_type():
    assert type('hello' is str)
    assert type('world' is not int)

def test_greater_and_less():
    assert 1 < 2
    assert 2 > 1

def test_list():
    num_list = [1, 2, 3]
    any_list = [False, False]
    assert 1 in num_list
    assert 4 not in num_list
    assert all(num_list)
    assert not any(any_list)



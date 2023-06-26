import pytest
import sys
# @pytest.mark.skip(reason = "To demo how to skip the perticular test")
# def test_demo1():
#     assert True
# @pytest.mark.skipif(sys.version_info == (3.6),reason="require python 3.6 or above")
# def test_demo2():
#     assert True
#
# def test_demo3():
#     assert True

@pytest.mark.windows
def test_windows1():
    assert True

@pytest.mark.windows
def test_windows2():
    assert True

@pytest.mark.mac
def test_mac1():
    assert True

@pytest.mark.mac
def test_mac2():
    assert True


# @pytest.mark.skip : skips the first test below it without displaying any reason
# @pytest.mark.skip(reason = "") :  skips the first test below it with displaying any reason
# pytest fileName -v -rxs  : to get reason at the terminal
# pytest fileName -k function/testName -v : to deselect the rest and run only perticular test

# @pytest.mark.name : to be written above the function
# pytest fileName -m name(ex: mac) -v
import pytest


def sum(a,b):
    return a+b

@pytest.mark.parametrize("input1,input2,output", [(2,3,5),(8,2,0),(2,1,3)])
def test_calc_sum1(input1,input2,output):
    result = sum(input1,input2)
    assert result == output
    # print("result is ", result)


# To avoid writing repitative func. we can use pytest parameterisation as above
# def test_calc_sum2():
#     result = sum(3,3)
#     assert result == 6
#
# def test_calc_sum3():
#     result = sum(5,3)
#     assert result == 8
#



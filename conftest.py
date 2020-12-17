import pytest


@pytest.fixture()  # 在方法前后执行
def oreder1():
    print("测试案例开始计算")

    yield
    print('测试案例结束计算')

@pytest.fixture(scope='module')  # 在方法前后执行
def oreder2():
    print("测试类开始进行")

    yield
    print('测试类执行完毕')
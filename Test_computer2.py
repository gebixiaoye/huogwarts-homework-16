from  computer import *
# from conftest import *
import pytest
import yaml

def getdate():
    return yaml.safe_load(open("testdata.yml"))


class Test_computer():

    @pytest.mark.parametrize('a,b,result',[
        (1,4,5),(-1,-22,-23)
    ])
    def test_add(self,oreder1,a,b,result):
        assert add(a,b) == result
        print("执行function的前置函数函数")

    @pytest.mark.parametrize("a,b,result",
                             getdate()["datas"]
        )
    def test_sub(self,oreder2,a,b,result):
        assert sub(a,b)== result
        print("执行module的前置行数")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,result', [
        (-2, -8, 16)
    ])
    def test_mul(self,a,b,result):
        assert mul(a,b)== result
        print("先乘")

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,result', [
        (12, 4, 3)
    ])
    def test_div(self,a,b,result):
        assert div(a,b)== result
        print("再除")

if __name__ == '__main__':
    Test_computer()
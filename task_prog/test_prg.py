import pytest
from task_prog.task import calculate

@pytest.mark.parametrize('number',
                         [
                            (200),
                            (54),
                            (23)
                         ])
def test_calculate(number):
    for i in calculate(number):
        assert eval(i) == number

if __name__ == "__main__":
    pytest.main()
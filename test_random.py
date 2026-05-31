# 自动生成的测试文件
# 运行方法: 在项目根目录运行 `pytest`（需要安装 pytest）

import pytest


def test_addition():
    assert 2 + 3 == 5


def test_string_reverse():
    assert "abc"[::-1] == "cba"


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0

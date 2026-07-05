import pytest

from week01_python.src.metrics import mae, mean, mse


def test_mean():
    assert mean([1, 2, 3]) == 2.0


def test_mae():
    assert mae([10, 20, 30], [12, 18, 33]) == 7 / 3


def test_mse():
    assert mse([10, 20, 30], [12, 18, 33]) == 17 / 3


def test_mean_empty_list():
    with pytest.raises(ValueError):
        mean([])


def test_mae_empty_lists():
    with pytest.raises(ValueError):
        mae([], [])


def test_mse_empty_lists():
    with pytest.raises(ValueError):
        mse([], [])


def test_mae_different_lengths():
    with pytest.raises(ValueError):
        mae([1, 2], [1])


def test_mse_different_lengths():
    with pytest.raises(ValueError):
        mse([1, 2], [1])
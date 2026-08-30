from module_01_python_engineering.src.preprocessing import clip_values


def test_clip_values_limits_numbers_to_range():
    result = clip_values([-2, 4, 11], 0, 10)

    assert result == [0, 4, 10]
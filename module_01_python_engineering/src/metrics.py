def mean(values: list[float]) -> float:
    if len(values) == 0:
        raise ValueError("List must not be empty")

    total = 0.0
    for value in values:
        total += value
    return total / len(values)


def mse(y_true: list[float], y_pred: list[float]) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Lists must have the same length")

    if len(y_true) == 0:
        raise ValueError("List must not be empty")

    error_sum = 0.0

    for true_value, predicted_value in zip(y_true, y_pred):
        error = true_value - predicted_value
        error_sum += error**2

    return error_sum / len(y_true)


def mae(y_true: list[float], y_pred: list[float]) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Lists must have the same length")

    if len(y_true) == 0:
        raise ValueError("List must not be empty")

    error_sum = 0.0

    for true_value, predicted_value in zip(y_true, y_pred):
        error_sum += abs(true_value - predicted_value)

    return error_sum / len(y_true)

def clip_values(values, lower, upper):
    if lower > upper: return ValueError
    else:
        res = []
        for i in range(len(values)):
            if lower < values[i] < upper:
                res.append(values[i])
        return res
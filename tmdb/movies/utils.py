def is_integer(value):
    try:
        int(value)
        return True
    except Exception:
        return False


def is_number(value):
    try:
        v1 = '.' in value
        float(value)
        return v1
    except Exception:
        return False

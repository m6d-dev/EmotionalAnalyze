import numpy as np


def convert_numpy_to_python(obj):
    if isinstance(obj, np.generic):  # np.float32, np.int64 и т.д.
        return obj.item()
    elif isinstance(obj, dict):
        return {k: convert_numpy_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_to_python(x) for x in obj]
    else:
        return obj

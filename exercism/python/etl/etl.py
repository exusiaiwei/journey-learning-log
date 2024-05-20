def transform(legacy_data):
    """Transform data of type {score: letters} to {letter: score}"""
    data = {}
    for k, v in legacy_data.items():
        for i in v:
            data[i.lower()] = k
    return data
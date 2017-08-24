def transform(data):
    result={}
    for key in data:
        for i in data[key]:
            result[i.lower()] = key
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):        
            result.append(item)
    return result
def capital_indexes( str ):
    result = []
    for i, v in enumerate(str):
        if (v.isupper()):
            result.append(i)
    return result
        
        
print(capital_indexes("HeLlO"))

print(capital_indexes("HI"))
# WAP to replace value present in nested dictionary. Replace "nose" with "net" ?

d= {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}

def replace_dict(dict_, old_, new_):
    for key, value in dict_.items():
        if isinstance(value, dict):
            for k, v in value.items():
                if v == old_:
                    value[k] = new_

    return dict_

res = replace_dict(d, 'nose', 'net')
print(res)

# output:-  {'a': 100, 'b': {'m': 'man', 'n': 'net', 'o': 'ox', 'c': 'cat'}}

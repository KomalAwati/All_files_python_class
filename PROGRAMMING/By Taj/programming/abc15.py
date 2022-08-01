# check given datatype is string or not
# 1
def check_datatype(string):
    if isinstance(string, str):
        return True
    return False
print(check_datatype('hello'))   #  True

# 2
def check_dt(string):
    return isinstance(string, str)

print(check_dt(12546))       #   False

# utils.py (H)
import re

var_num_or_dot_regex = re.compile(r'^[0-9.]$')

def func_isnumordot(string: str):
    return bool(var_num_or_dot_regex.search(string))

def func_isempty(string: str):
    return len(string) == 0

def func_isvalidnumber(string: str):
    var_valid = False
    try:
        float(string)
        var_valid = True
    except ValueError:
        var_valid = False
    return var_valid

# utils.py (H)

import re

var_num_or_dot_regex = re.compile(r'^[0-9.]$')

def func_isnumordot(string: str):
    return bool(var_num_or_dot_regex.search(string))

def func_isempty(string: str):
    return len(string) == 0
# utils.py (H)
import re #1:

var_num_or_dot_regex = re.compile(r'^[0-9.]$') #2:

def func_isnumordot(string: str): #3:
    return bool(var_num_or_dot_regex.search(string))

def func_isempty(string: str): #4:
    return len(string) == 0

def func_converttointorfloat(string: str): #5:
    var_number = float(string)

    if var_number.is_integer():
        var_number = int(var_number)
    return var_number

def func_isvalidnumber(string: str): #6:
    var_valid = False
    try:
        float(string)
        var_valid = True
    except ValueError:
        var_valid = False
    return var_valid

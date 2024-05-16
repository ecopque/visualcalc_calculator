# variables.py (C)
from pathlib import Path #1:

PATH_ROOT_FOLDER = Path(__file__).parent #2:
PATH_FILES_DIR = PATH_ROOT_FOLDER / 'files' #3:
PATH_WINDOW_ICON_PATH = PATH_FILES_DIR / 'ecop.png' #4:

var_big_font_size = 40 #5:
var_medium_font_size = 24 #5:
var_small_font_size = 18 #5:
var_text_margin = 15 #5:
var_minimum_width = 450 #5:

var_primary_color = '#1e81b0' #6:
var_primary_color_red = '#FF3333' #6:
var_darker1_primary_color = '#16658a' #6:
var_darker2_primary_color = '#115270' #6:

# styles.py (F)
# pip install pyqtdarktheme
import qdarktheme
from variables import var_primary_color, var_darker1_primary_color, var_darker2_primary_color

var_qss =  f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {var_primary_color};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {var_darker1_primary_color};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {var_darker2_primary_color};
    }}
"""

def func_setuptheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{var_primary_color}",
            },
            "[light]": {
                "primary": f"{var_primary_color}",
            },
        },
        additional_qss=var_qss
    )

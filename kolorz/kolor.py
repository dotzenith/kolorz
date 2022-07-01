"""
A library to facilitate printing colored output to terminals
"""
from kolorz.colors import colors
from typing import Optional, Any
from dotwiz import DotWiz

def make_kolorz(colorscheme: str = "catppuccin mocha", custom: Optional[dict[Any, Any]] = None):
    """
    Instantiates a custom dotwiz dict with kolorz
    """
    if custom is None:
        theme = colors[colorscheme]
    else:
        theme = custom
    
    kolorz_dict = {color_name: make_kolor(color_value) for color_name, color_value in theme.items()}
    kolorz_dict['end'] = "\033[0m"

    return DotWiz(kolorz_dict)

def make_kolor(color: tuple) -> str:
    """
    Wraps the rgp tuple in an escape sequence 
    """
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m"

def get_all_colorschemes() -> list[str]:
    """
    Returns a list of all all available colorschemes
    """
    return list(colors.keys())

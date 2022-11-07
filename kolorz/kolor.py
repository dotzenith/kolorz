"""
A library to facilitate printing colored output to terminals
"""
from typing import Any, Optional

from dotwiz import DotWiz

from kolorz.colors import colors


def make_kolorz(
    colorscheme: str = "catppuccin mocha",
    custom: Optional[dict[Any, Any]] = None,
    num_colors: bool = False,
) -> DotWiz:
    """
    Instantiates a custom dotwiz dict with kolorz

    :param colorscheme: The name of the colorscheme
    :param custom: A custom set of colors
    :param num_colors: Use if numbered colors are prefered instead of named colors
    """
    if custom is None:
        theme = colors[colorscheme]
    else:
        theme = custom

    kolorz_dict = {
        color_name: make_kolor(color_value) for color_name, color_value in theme.items()
    }
    kolorz_dict["end"] = "\033[0m"

    if num_colors:
        # I could do a dict comprehension here but not doing so because of readability
        new_kolorz_dict = {}
        for color_index, (color_name, color) in enumerate(kolorz_dict.items()):
            if color_name == "white" or color_name == "end":
                new_kolorz_dict[color_name] = color
            else:
                new_kolorz_dict[f"color{color_index}"] = color

        new_kolorz_dict["end"] = "\033[0m"

        return DotWiz(new_kolorz_dict)

    return DotWiz(kolorz_dict)


def make_kolor(color: tuple) -> str:
    """
    Wraps the rgb tuple in an escape sequence
    """
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m"


def get_all_colorschemes() -> list[str]:
    """
    Returns a list of all all available colorschemes
    """
    return list(colors.keys())

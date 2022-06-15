"""
A library to facilitate printing colored output to terminals
"""
from kolorz.colors import colors
from typing import Optional, Any

class kolorz:
    """
    The koolest klass you've ever seen
    """
    def __init__(self, colorscheme: str = "catppuccin mocha", custom: Optional[dict[Any, Any]] = None) -> None:
        
        if custom is None:
            self.colorscheme = colorscheme
            theme = colors[colorscheme]
        else:
            self.colorscheme = "custom"
            theme = custom

        for key, val in theme.items():
            setattr(self, key, self._assign_color(val)) 
            
        self.end = "\033[0m"

    def __str__(self) -> str:
        return f"Current Colorscheme: {self.colorscheme}"        

    def _assign_color(self, color: tuple) -> str:
        """
        Wraps the rgp tuple in an escape sequence 
        """
        return f"\033[38;2;{color[0]};{color[1]};{color[2]}m"

    def set_color(self, color: str, color_values: tuple) -> None:
        """
        overrides an existing color. 

        If the specified color does not exist, makes a new one
        """
        setattr(self, color, self._assign_color(color_values))


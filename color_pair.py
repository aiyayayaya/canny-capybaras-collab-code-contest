from enum import Enum


class ColorPair(Enum):
    """
    Enumerate color pair numbers

    Naming Scheme: fg_on_bg
    """

    black_on_white = 1
    red_on_black = 2
    blue_on_black = 3
    green_on_black = 4
    white_on_black = 5

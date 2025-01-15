import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor





class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0"
    MEDIUM = "3"
    DEFAULT = "4"
    BIG = "5"
    BUTTON = "3"
    VERY_BIG = "9"


STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap",
    "https://fonts.googleapis.com/css2?family=Fira+Code:wght@300..700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto&display=swap"
]

BASE_STYLE = {
    "font_family": Font.Poppins_Fonts.value,
    "color": TextColor.TERTIARY.value,
    "background": Color.PRIMARY.value,
    rx.heading: {
        "font_family": Font.Poppins_Fonts.value,
        "color": TextColor.TERTIARY.value
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none"
        }
    },
    rx.el.span: {
        "font_size": Size.MEDIUM.value,
        "color": TextColor.SECONDARY.value
    },
    rx.button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BUTTON.value,
        "color": f"{TextColor.SECONDARY.value} !important",
        "_hover": {
            "color": f"{TextColor.PRIMARY.value} !important"
        }
    },
    
    
}
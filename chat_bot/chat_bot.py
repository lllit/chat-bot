import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import reflex as rx

# ------- IMPORT PAGES----
from chat_bot.pages.chat import chat_view
from chat_bot.pages.about import about
from chat_bot.pages.home import home_view
from chat_bot.pages.chat_arriendos import chat_arriendos_view


import chat_bot.styles.styles as styles

# --- APP ---


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    html_lang='es',
    theme=rx.theme(
        appearance="dark",
        accent_color="violet"
    )
)


app.add_page(
    home_view, 
    title="Home", 
    route="/",
    image="favicon.ico"
)

app.add_page(
    chat_view, 
    title="Chat Bot",
    route="/chat",
    image="favicon.ico"
)

app.add_page(
    chat_arriendos_view,
    title="Chat Arriendos",
    route="/chat_arriendos",
    image="favicon.ico"
)


app.add_page(
    about,
    title="About", 
    route="/about",
    image="favicon.ico"
)

import reflex as rx

from chat_bot.views.navbar import navbar

from chat_bot.components.vista_header import vista_header
from chat_bot.components.template_card import template_card



def home_view() -> rx.Component:
    return rx.container(
        navbar(),
        vista_header(
            titulo_header="Home Page", 
            subtitle="This is the home page of the Chat Bot application."
        ),
        
        rx.box(
            rx.link(
                template_card(
                    "message-circle",
                    "Hazle un pregunta a tu base de datos",
                    "¿Cuantos usuarios tengo registrado?",
                    "grass",
                ),
                padding=0,
                href="/chat",
                is_external=False,
                class_name="inline-block"
            ),
            rx.link(
                template_card(
                    "badge-info",
                    "Sobre esta aplicación",
                    "Dejanos feedback",
                    "tomato",
                ),
                padding=0,
                href="/about",
                is_external=False,
                class_name="inline-block"
            ),
            wrap="wrap",
            class_name="p-5 gap-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 ",
        ),
        padding=0,
    )

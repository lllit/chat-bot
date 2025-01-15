import reflex as rx

from chatbot.views.navbar import navbar

from chatbot.components.vista_header import vista_header
from chatbot.components.template_card import template_card



def home_view() -> rx.Component:
    return rx.container(
        navbar("Chat Bot"),
        vista_header(
            titulo_header="Asistentes", 
            subtitle="Es una pagina que respondera"
        ),
        
        rx.box(
            rx.link(
                template_card(
                    "message-square-code",
                    "Asistente Codes LLLIT",
                    "codeslllit asistente",
                    "grass",
                ),
                padding=0,
                href="/chat",
                is_external=False,
                style={"display": "contents"}
            ),
            rx.link(
                template_card(
                    "briefcase",
                    "Asistente Arriendos",
                    "Consultas sobre disponibilidad",
                    "grass",
                ),
                padding=0,
                href="/chat_arriendos",
                is_external=False,
                style={"display": "contents"}
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
                style={"display": "contents"}
            ),
            wrap="wrap",
            class_name="p-2 grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-2",
        ),
        padding=0,
    )

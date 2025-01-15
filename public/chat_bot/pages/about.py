import reflex as rx

from chatbot.views.navbar import navbar

from chatbot.components.vista_header import vista_header

def about() -> rx.Component:
    return rx.container(
        navbar("About Chat Bot"),
        vista_header(titulo_header="About Page", subtitle="This is the about page of the Chat Bot application."),
        class_name="p-10",
        padding=0
    )

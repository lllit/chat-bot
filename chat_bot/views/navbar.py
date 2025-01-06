import reflex as rx

# --------- NAVBAR ------------
def navbar(titulo) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.icon("banana", size=25),
            href="/",
        ),
        
        rx.hstack(
            rx.heading(titulo, position="top-left", size="3"),
            align="center",
            justify="center",
            width="100%",
        ),
        rx.flex(
            rx.link(
                rx.icon("message-square-code"),
                href="/chat",
                is_external=False
            ),
            rx.link(
                rx.icon("briefcase"),
                href="/chat_arriendos",
                is_external=False
            ),
            rx.link(
                rx.icon("badge-info"),
                href="/about",
                is_external=False
            ),
            spacing="4"
        ),
        
        class_name="mb-5 mt-7 pl-5 pr-5",
        align="center",
        justify="between",
        width="100%",
    ),        
        
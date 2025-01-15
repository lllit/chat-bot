import reflex as rx

def vista_header(titulo_header, subtitle) -> rx.Component:
    return rx.container(
        rx.heading(titulo_header, align="center", class_name="mb-4"),
        rx.text(subtitle),
        class_name="pt-10 pb-10"
    ),
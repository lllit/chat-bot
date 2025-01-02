"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import aiohttp
import asyncio
import reflex as rx
from .utils.send_text_api import send_text_to_api, get_access_token

from rxconfig import config


USERNAME_API = os.getenv("USERNAME_API")
PASSWORD_API = os.getenv("PASSWORD_API")  

class FormInputState(rx.State):
    form_data: dict = "Esperando respuesta..."
    response_data: str = "Esperando respuesta..."


    @rx.event
    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.response_data = "Esperando respuesta..."

        token = await get_access_token(USERNAME_API, PASSWORD_API)
        response = await send_text_to_api(data=self.form_data, token=token)

        self.response_data = response
        
        print("Self Response", self.response_data)

        
        



def form_input1():
    return rx.card(
        rx.vstack(
            rx.heading("💿 BOT SQL", align="center", class_name="pt-5"),
            rx.divider(),
            #------- VISTA RESPUESTA ---------
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="banana"),
                    rx.scroll_area(
                        rx.flex(
                            rx.html(
                                FormInputState.response_data.to_string(),
                            ),
                            direction="column",
                            spacing="4",
                        ),
                        type="hover",
                        scrollbars="vertical",
                        style={"max-height": "500px"},
                    ),
                    align="stretch"
                ),
                spacing="5",
                class_name="mb-10 mt-5"
            ),
            # -------- BOTON DE ENVIO ------------
            rx.form.root(
                rx.center(
                    rx.el.input(
                        name="human_query",
                        placeholder="Pregunta aqui...",
                        type="text",
                        required=True,
                        class_name="box-border bg-slate-3 px-4 py-2 pr-14 rounded-full w-full outline-none focus:outline-accent-10 h-[48px] text-slate-12 placeholder:text-slate-9",
                    ),
                    rx.el.button(
                        "Enviar", 
                        type="submit",
                        size='3',
                        class_name="box-border px-5 py-2 bg-slate-700 rounded-full ml-3"
                    ),
                    width="100%",
                ),
                on_submit=FormInputState.handle_submit,
                reset_on_submit=True,
            ),
            align_items="center",
            width="100%",
            
        ),
        width="100%",
        class_name="mt-10"
        
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            form_input1(),
            spacing="5",
            justify="start",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)

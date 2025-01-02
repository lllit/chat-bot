import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import aiohttp
import asyncio
import reflex as rx
from .utils.send_text_api import send_text_to_api, get_access_token
import uuid
from rxconfig import config
 
import chat_bot.styles.styles as styles

USERNAME_API = os.getenv("USERNAME_API")
PASSWORD_API = os.getenv("PASSWORD_API")  

class FormInputState(rx.State):
    form_data: dict = "Esperando pregunta..."
    response_data: list[tuple[str, str]] = [("Esperando respuesta...", "")]
    processing: bool = False
    user_id: str = str(uuid.uuid4())

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.form_data = form_data.get("human_query", "")
        #self.response_data.append("Esperando respuesta...")
        self.response_data.append((self.form_data, "Esperando pregunta..."))
        self.processing = True
        yield

        token = await get_access_token(USERNAME_API, PASSWORD_API)
        response = await send_text_to_api(data={"human_query": self.form_data}, token=token)

        self.response_data[-1] = (self.form_data, response)

        print("Response_data[-1] ", self.response_data[-1])


        print("Self Response", self.response_data)
        self.processing = False
        yield

    def clear_chat(self):
        self.response_data = ["Esperando respuesta..."]
        self.processing = False

        
        



def form_input1():
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.icon("banana", size=30),
                rx.heading("BOT SQL", align="center"),
                class_name="mb-5 mt-5 pl-5 pr-5",
                align="center",
                justify="between",
                width="100%",
            ),
            
            rx.divider(),
            #------- VISTA RESPUESTA ---------
            rx.vstack(
                rx.hstack(
                    rx.scroll_area(
                        rx.flex(
                            rx.foreach(FormInputState.response_data, lambda pair: rx.vstack(
                                rx.hstack(
                                    rx.icon(tag="chevron-right"),
                                    rx.html(f"{pair[0]}"),
                                    align="start",
                                    justify="start",
                                    class_name="text-left",
                                    wrap='nowrap',
                                ),
                                rx.hstack(
                                    rx.html(f"{pair[1]}"),
                                    rx.icon(tag="chevron-left"),
                                    align="start",
                                    justify="end",
                                    class_name="text-right",
                                    wrap='nowrap',
                                ),
                                width="100%",
                                direction="column",
                                spacing="5",
                                class_name="mb-4 w-full",
                                align="stretch",
                                justify="between"
                                ),
                                
                            ),
                            width="100%",
                            direction="column",
                            spacing="4",
                        ),
                        width="100%",
                        type="hover",
                        scrollbars="vertical",
                        style={"max-height": "500px"},
                        
                    ),
                    width="100%",
                    align="stretch",
                ),
                width="100%",
                justify="between",
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
        class_name="mt-10",
    )


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            form_input1(),
            spacing="5",
            justify="between",
            min_height="85vh",
        ),
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    html_lang='es'
)
app.add_page(
    index, 
    title="Chat Bot"
)


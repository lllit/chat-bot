import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import reflex as rx
import uuid

from chatbot.utils.send_text_api import send_text_to_api, get_access_token

from chatbot.views.navbar import navbar


USERNAME_API = os.getenv("USERNAME_API")
PASSWORD_API = os.getenv("PASSWORD_API")  

# --- ESTADOS ----

class FormInputState(rx.State):
    form_data: str = ""
    response_data: list[tuple[str, str]] = []
    processing: bool = False
    user_id: str = str(uuid.uuid4())

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.form_data = form_data.get("human_query", "")
        self.response_data.append((self.form_data, "Esperando respuesta..."))
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


   
# -------- BOTON DE ENVIO ------------
def input_form() -> rx.Component:
    return rx.form.root(
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
            class_name="absolute bottom-0 left-0 w-full p-4 mb-4 mt-4"
        ),


# --------- VISTA RESPUESTA --------------
def respuesta_old() -> rx.Component:
    return rx.card(
        rx.vstack(
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
            
            align_items="center",
            width="100%",
            
        ),
        width="100%",
        class_name="mt-10",
    )






#------- VISTA RESPUESTA ---------
def respuesta() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.scroll_area(
                    rx.flex(
                        rx.foreach(FormInputState.response_data, lambda pair: rx.vstack(
                            # PREGUNTA
                            rx.hstack(
                                rx.box(
                                    rx.icon(tag="chevron-right"),
                                    class_name="align-start"
                                ),
                                
                                rx.markdown(f"{pair[0]}"),
                                align="start",
                                justify="start",
                                class_name="text-left",
                                wrap='nowrap',
                            ),
                            # RESPUESTA
                            rx.hstack(
                                rx.markdown(
                                    pair[1].replace("<br>", "\n") if isinstance(pair[1], str) else pair[1],
                                    class_name="[&>p]:!my-2.5"
                                ),
                                rx.box(
                                    rx.icon(tag="chevron-left"),
                                    class_name="align-start",
                                ),
                                align="start",
                                justify="end",
                                class_name="text-right",
                                wrap='nowrap',
                            ),
                            width="100%",
                            direction="column",
                            spacing="5",
                            class_name="mb-0 w-full pl-3 pr-3",
                            align="stretch",
                            justify="between"
                            ),
                            
                        ),
                        width="100%",
                        direction="column",
                        spacing="4",
                        justify="center",
                        style={".rt-r-ai-start": {"align-items": "center"}}
                    ),
                    width="100%",
                    type="hover",
                    scrollbars="vertical",
                    style={"max-height": "70vh"},
                ),
                width="100%",
                align="stretch",
            ),
            width="100%",
            justify="between",
            spacing="5",
        ),
        align_items="center",
        width="100%",
        class_name="mt-5 mb-10",
    )


# ----- VISTA GENERAL -----

def chat_view() -> rx.Component:
    return rx.container(
        rx.vstack (
            navbar("Asistente Codes"),
            rx.divider(),
            respuesta(),
            input_form(),
            class_name="relative overflow-hidden",
            min_height="100vh",
            padding="0", 
        ),
        padding="0",
        class_name="relative overflow-y-hidden"
    )
        
import reflex as rx

def template_card(icon: str, title: str, description: str, color: str) -> rx.Component:
    return rx.el.button(
        rx.hstack(
            rx.icon(tag=icon, color=rx.color(color, 9), size=36),
            rx.text(title, class_name="font-medium text-slate-11 text-sm"),
            direction="row",
            align="center"
        ),
        rx.text(description, class_name="text-slate-10 text-xs"),
        class_name="relative align-top flex flex-col gap-2 border-slate-4 bg-slate-1 hover:bg-slate-3 shadow-sm px-3 pt-3 pb-4 border rounded-2xl text-[15px] text-start transition-colors",
    )
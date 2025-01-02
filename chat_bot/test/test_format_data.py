def format_response_text(response_data: dict) -> str:
    message = response_data.get('message', 'No response received')
    formatted_message = message.replace('\n', '<br>')
    return formatted_message

# Ejemplo de uso
response_data = {
    "message": "¡Claro! Según la información disponible en nuestra base de datos, los nombres de tus usuarios son los siguientes:\n\n* Matias\n* Manfred\n* Stefan\n* Jun\n* An\n* test\n* Mzwakhe\n* Erik\n* Geert\n* Herman\n* Florence\n* Martin\n* Tolis\n* Emmanuel\n* enzo\n* Manfred\n* Alessandro\n\nEspero que esto sea lo que estabas buscando. ¡Si necesitas algo más, no dudes en preguntar!"
}

formatted_text = format_response_text(response_data)
print(formatted_text)
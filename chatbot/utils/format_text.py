

def format_response_text(response_data: dict) -> str:
    message = response_data.get('message', 'No response received')
    formatted_message = message.replace('\n', '<br>')
    return formatted_message
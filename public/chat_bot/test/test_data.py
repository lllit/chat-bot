import requests



# Datos que quieres enviar a tu API


data = {
    "human_query": "¿Cuál es la capital de Francia?"
}


def send_text_to_api(data: dict):
    try:
        # URL de tu API
        url = "http://127.0.0.1:9000/human_query"

        # Enviar la solicitud POST
        response = requests.post(url, json=data)
        
        # Verificar el estado de la respuesta
        if response.status_code == 200:
            print("Respuesta de la API:", response.json())
        else:
            print("Error al comunicarse con la API:", response.status_code, response.text)


    except requests.exceptions.RequestException as e:
        print("Error al intentar conectar con la API:", e)


send_text_to_api(data=data)
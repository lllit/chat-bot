import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import requests
import json
import asyncio
import aiohttp
from .format_text import format_response_text

from dotenv import load_dotenv
import os

load_dotenv()

USERNAME_API = os.getenv("USERNAME_API")
PASSWORD_API = os.getenv("PASSWORD_API")  

URL_API = os.getenv("URL_API")

# ---------- Obtener acceso a mi api ------------

async def get_access_token(username: str, password: str) -> str:
    try:
        url = f"{URL_API}/token"
        data = {
            "username": username,
            "password": password
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result["access_token"]
                else:
                    raise Exception("Failed to obtain access token")
    except aiohttp.ClientError as e:
        print("Error al intentar conectar con la API:", e)
        return {"message": "Error al conectar con la API"}




data = {
    "human_query": "¿Cuál es la capital de Francia?"
}

# ---------- Enviar texto a mi api ------------

async def send_text_to_api(data: dict, token: str):
    try:
        # URL de tu API
        url = f"{URL_API}/human_query"

        headers = {
            "Authorization": f"Bearer {token}"
        }

        # Enviar la solicitud POST con el token de acceso
        response = requests.post(url, json=data, headers=headers)
        
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                if response.status == 200:
                    result_dict = await response.json()

                    print("RESULT DICT: ",result_dict['message'])

                    format_text = format_response_text(result_dict)

                    return result_dict
                else:
                    print("Error al comunicarse con la API:", response.status_code, response.text)
                    raise Exception("Failed to send text to API")




    except requests.exceptions.RequestException as e:
        print("Error al intentar conectar con la API:", e)

        reponse = {"message":"Error al conectar con la api"}

        return reponse



# ----------- TEST ---------------

import icalendar
import requests
from pathlib import Path
import json


def arriendo_json():
    # URL del archivo .ics
    url = "https://www.airbnb.cl/calendar/ical/31351779.ics?s=b33143189db89132f106f3939522c5da"


    # Descargar el archivo .ics
    response = requests.get(url)
    ics_content = response.content

    # Crear la carpeta temp_calendar si no existe
    temp_calendar_dir = Path("temp_calendar")
    temp_calendar_dir.mkdir(exist_ok=True)

    # Guardar el archivo .ics en la carpeta temp_calendar
    ics_path = temp_calendar_dir / "listing-31351779.ics"
    ics_path.write_bytes(ics_content)


    #ics_path = Path("listing-31351779.ics")

    with ics_path.open() as f:
        calendar = icalendar.Calendar.from_ical(f.read())

    contador = 1

    dias_arriendo_totales = 0

    arriendos = []

    for event in calendar.walk('VEVENT'):
        if event.get("SUMMARY") == "Airbnb (Not available)":
            break



        dtstart = event.get("DTSTART").dt
        dtend = event.get("DTEND").dt

      
        # Calcular la cantidad de días de arriendo
        dias_arriendo = (dtend - dtstart).days
        
        dias_arriendo_totales += dias_arriendo

        arriendo = {
            "Arriendo N°": contador,
            "Fecha Inicio": str(dtstart),
            "Fecha Fin": str(dtend),
            "Días de arriendo": dias_arriendo
        }
        arriendos.append(arriendo)


        
        
        contador += 1

    arriendos.append({"Dias totales arrendados": dias_arriendo_totales})

    return arriendos


# En el caso de que quiera guardar el esquema en un json
def guardar_json(temp_calendar_dir, arriendos):
    # Guardar los datos en un archivo JSON
    json_path = temp_calendar_dir / "arriendos.json"
    with json_path.open("w", encoding="utf-8") as json_file:
        json.dump(arriendos, json_file, ensure_ascii=False, indent=4)

    # Leer y mostrar el contenido del archivo JSON
    with json_path.open("r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        print(json.dumps(data, ensure_ascii=False, indent=4))




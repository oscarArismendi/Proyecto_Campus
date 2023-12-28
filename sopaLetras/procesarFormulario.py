from bs4 import BeautifulSoup

# Ruta al archivo HTML local
archivo_html = "C:/Users/user/Desktop/carpeta de chulo/programacióm/ejecuciónes/kali Linux/Proyecto_Campus/sopaLetras/index.html"

# Lee el contenido del archivo HTML
with open(archivo_html, "r", encoding="utf-8") as archivo:
    contenido_html = archivo.read()

# Parsea el HTML
soup = BeautifulSoup(contenido_html, 'html.parser')

# Encuentra el elemento de párrafo con el ID 'title'
paragraph_element = soup.find('p', {'id': 'title'})

# Verifica si se encontró el elemento
if paragraph_element is not None:
    # Obtiene el texto del párrafo
    paragraph_text = paragraph_element.get_text(strip=True)
    print("Texto del párrafo:", paragraph_text)
else:
    print("Elemento no encontrado con el ID 'title'")

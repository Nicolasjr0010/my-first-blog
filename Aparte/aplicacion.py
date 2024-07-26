import mysql.connector

# Configuración de la conexión
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'CVO2024',
    'database': 'compuxela'
}

# Conectar a la base de datos
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Consultar datos de la tabla Consolas
query = "SELECT codigo, nombre, modelo, fabricante, descripcion, precio FROM consolas"
cursor.execute(query)

# Obtener los resultados
productos = cursor.fetchall()

# Cerrar la conexión
cursor.close()
conn.close()

# Crear archivo HTML
with open("Consolas.html", "w") as file:
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<title>Lista de Consolas</title>\n")
    file.write("<style>\n")
    file.write("body { font-family: 'Roboto', sans-serif; margin: 0; padding: 0; background-color: #111; color: #e0e0e0; }\n")
    file.write("h1 { color: #00bfae; text-align: center; padding: 20px; }\n")
    file.write(".menu { max-width: 1200px; margin: auto; padding: 20px; }\n")
    file.write(".menu-item { cursor: pointer; padding: 15px; background-color: #222; margin: 5px 0; border-radius: 5px; }\n")
    file.write(".menu-item:hover { background-color: #333; }\n")
    file.write(".product-details { display: none; background-color: #333; padding: 15px; border-radius: 5px; margin-top: 10px; }\n")
    file.write(".product-details img { max-width: 300px; height: auto; border-radius: 5px; }\n")
    file.write(".product-details strong { color: #00bfae; }\n")
    file.write("</style>\n")
    file.write("<script>\n")
    file.write("function toggleDetails(id) {\n")
    file.write("  var element = document.getElementById(id);\n")
    file.write("  if (element.style.display === 'none') {\n")
    file.write("    element.style.display = 'block';\n")
    file.write("  } else {\n")
    file.write("    element.style.display = 'none';\n")
    file.write("  }\n")
    file.write("}\n")
    file.write("</script>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<h1>Lista de Consolas</h1>\n")
    file.write("<div class='menu'>\n")
    
    for index, producto in enumerate(productos):
        codigo, nombre, modelo, fabricante, descripcion, precio = producto
        file.write(f"<div class='menu-item' onclick='toggleDetails(\"product-{index}\")'>\n")
        file.write(f"{nombre}\n")
        file.write(f"</div>\n")
        file.write(f"<div id='product-{index}' class='product-details'>\n")
        file.write(f"<strong>Código:</strong> {codigo}<br>\n")
        file.write(f"<strong>Nombre:</strong> {nombre}<br>\n")
        file.write(f"<strong>Modelo:</strong> {modelo}<br>\n")
        file.write(f"<strong>Fabricante:</strong> {fabricante}<br>\n")
        file.write(f"<strong>Descripción:</strong> {descripcion}<br>\n")
        file.write(f"<strong>Precio:</strong> ${precio:.2f}<br>\n")
        file.write(f"<img src='C:\\Users\\andre\\OneDrive\\Progra Python\\myvenvo\\djangogirls\\Media\\Beef-Tacos.jpg' alt='Foto de {nombre}'><br>\n")
        file.write(f"</div>\n")
    
    file.write("</div>\n")
    file.write("</body>\n")
    file.write("</html>\n")

print("Archivo HTML creado exitosamente.")
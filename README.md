# 📇 Agenda de Contactos - Python & MySQL

Sistema de gestión de contactos (CRUD) desarrollado en Python con persistencia de datos en una base de datos MySQL.

## ✨ Características
- **Crear:** Registro de nuevos contactos con nombre, apellido, email, teléfono y cumpleaños.
- **Listar:** Visualización de todos los contactos guardados.
- **Modificar:** Edición dinámica de datos existentes (permite mantener valores actuales).
- **Eliminar:** Borrado de registros mediante ID único.
- **Buscar:** Filtro de búsqueda por nombre o apellido.
- **Interfaz:** Consola limpia con pausas de lectura y limpieza de pantalla automática.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Base de Datos:** MySQL
- **Librería:** `mysql-connector-python`

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone [https://github.com/josemanuelrbdev-crypto/agenda-python-mysql.git](https://github.com/josemanuelrbdev-crypto/agenda-python-mysql.git)


2. Instalar dependencias
Asegúrate de tener instalada la librería necesaria para conectar Python con MySQL:

Bash
pip install mysql-connector-python



3. Configurar la Base de Datos
Importa el archivo BD.sql en tu servidor MySQL o ejecuta los siguientes comandos:

SQL
CREATE DATABASE agenda_db;
USE agenda_db;

CREATE TABLE contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(20),
    cumpleanos VARCHAR(50)
);


4. Ejecutar la aplicación
Bash
python crud.py


📝 Notas
Asegúrate de configurar correctamente el usuario y la contraseña de tu MySQL en la función get_connection() dentro del archivo crud.py.

Python
connection = mysql.connector.connect(
    host='localhost',
    user='tu_usuario',
    password='tu_password',
    database='agenda_db'
)


---

### Pasos finales:
1. Después de pegar el texto, baja hasta el final de la página.
2. Verás un cuadro que dice **"Commit changes..."**.
3. Escribe un mensaje corto como *"Añadir README detallado"* y dale clic al botón verde de **"Commit changes"**.

¡Listo! Ahora tu repositorio tiene una presentación de lujo que cualquiera puede entender y usar. 🚀 ¿Qué te parece cómo quedó?

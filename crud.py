import os
import time
import mysql.connector
from mysql.connector import Error

# 1. Configuración de la conexión a MySQL
def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',      # Tu usuario de MySQL (por defecto es root)
            password='',      # Tu contraseña de MySQL
            database='agenda_db'
        )
        return connection
    except Error as e:
        print(f"\n[ERROR] No se pudo conectar a MySQL: {e}")
        input("Presiona Enter para reintentar...")
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 2. Función para crear contacto
def create_contact():
    clear_screen()
    print('--- Nuevo Contacto ---')
    name = input('Nombre: ')
    surname = input('Apellido: ')
    email = input('Email: ')
    phone = input('Teléfono: ')
    birthday = input('Cumpleaños: ')

    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO contactos (nombre, apellido, email, telefono, cumpleanos) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, surname, email, phone, birthday))
        conn.commit()
        print('\n¡Contacto guardado con éxito!')
        conn.close()
    
    input('\nPresiona Enter para volver al menú...')

# 3. Función para listar contactos
def list_contacts(wait=True):
    clear_screen()
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, apellido, telefono, email FROM contactos")
        rows = cursor.fetchall()
        
        if not rows:
            print('\nLa agenda está vacía.')
        else:
            print('\n' + '-'*10 + ' LISTA DE CONTACTOS ' + '-'*10)
            for row in rows:
                print(f"ID: {row[0]} | {row[1]} {row[2]} | Tel: {row[3]} | Email: {row[4]}")
            print('-' * 40)
        
        conn.close()
    
    if wait:
        input('\nPresiona Enter para volver al menú...')

# 4. Función para editar contacto
def edit_contact():
    list_contacts(wait=False)
    try:
        contact_id = int(input('\nIntroduce el ID del contacto a editar (o 0 para cancelar): '))
        if contact_id == 0: return

        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contactos WHERE id = %s", (contact_id,))
            contact = cursor.fetchone()

            if contact:
                print(f"\nEditando: {contact[1]} {contact[2]}")
                print("Presiona Enter para mantener el valor actual.")
                
                # Si el input está vacío, usa el valor original
                n_name = input(f"Nombre [{contact[1]}]: ") or contact[1]
                n_surname = input(f"Apellido [{contact[2]}]: ") or contact[2]
                n_email = input(f"Email [{contact[3]}]: ") or contact[3]
                n_phone = input(f"Teléfono [{contact[4]}]: ") or contact[4]
                n_bday = input(f"Cumpleaños [{contact[5]}]: ") or contact[5]

                query = "UPDATE contactos SET nombre=%s, apellido=%s, email=%s, telefono=%s, cumpleanos=%s WHERE id=%s"
                cursor.execute(query, (n_name, n_surname, n_email, n_phone, n_bday, contact_id))
                conn.commit()
                print('\n¡Contacto actualizado correctamente!')
            else:
                print('ID no encontrado.')
            conn.close()
    except ValueError:
        print('Entrada no válida.')
    
    input('\nPresiona Enter para continuar...')

# 5. Función para eliminar contacto
def delete_contact():
    list_contacts(wait=False)
    try:
        contact_id = int(input('\nID del contacto a eliminar (0 para cancelar): '))
        if contact_id == 0: return

        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contactos WHERE id = %s", (contact_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f'Contacto {contact_id} eliminado.')
            else:
                print('No se encontró el ID.')
            conn.close()
    except ValueError:
        print('ID no válido.')
    
    input('\nPresiona Enter para continuar...')

# 6. Función para buscar contacto
def search_contact():
    clear_screen()
    search = input('Nombre a buscar: ')
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM contactos WHERE nombre LIKE %s OR apellido LIKE %s"
        cursor.execute(query, (f'%{search}%', f'%{search}%'))
        results = cursor.fetchall()
        
        if results:
            print(f"\n--- Resultados para '{search}' ---")
            for r in results:
                print(f"ID: {r[0]} | {r[1]} {r[2]} | Tel: {r[4]}")
        else:
            print("No se encontraron coincidencias.")
        conn.close()
    
    input('\nPresiona Enter para continuar...')

# 7. Ejecución principal
def run():
    while True:
        clear_screen()
        print('\n' + '*' * 20 + ' AGENDA MYSQL ' + '*' * 20)
        print('[C]rear | [L]istar | [M]odificar | [E]liminar | [B]uscar | [S]ALIR')
        print('*' * 54)
        command = input('-> ').upper()

        if command == 'C':
            create_contact()
        elif command == 'L':
            list_contacts()
        elif command == 'M':
            edit_contact()
        elif command == 'E':
            delete_contact()
        elif command == 'B':
            search_contact()
        elif command == 'S':
            print('\nSaliendo del sistema...')
            break
        else:
            print('\nOpción no válida.')
            time.sleep(1)

if __name__ == "__main__":
    run()
# Cheems API – Sistema de Tickets de Soporte Técnico

API hecha con Django para registrar y dar seguimiento a tickets de soporte técnico.

La API recibe peticiones HTTP, guarda los tickets en una base de datos SQLite y responde en formato JSON. Permite crear, listar, consultar, editar y eliminar tickets (CRUD), y valida los datos antes de guardarlos, regresando mensajes personalizados cuando algo está mal.

Cada ticket tiene título, descripción, prioridad (alta, media o baja), estado (abierto, en progreso o cerrado) y fecha de creación. Un ticket cerrado ya no se puede modificar.

## Cómo correrlo

Con el entorno virtual activado:

1. Crear las tablas en tu base de datos:

   ```
   python manage.py migrate
   ```

2. (Opcional) Crear un usuario para el panel de administración:

   ```
   python manage.py createsuperuser
   ```

3. Levantar el servidor:
   ```
   python manage.py runserver
   ```

La API queda disponible en `http://127.0.0.1:8000/`.
El panel de administración está en `http://127.0.0.1:8000/admin/`.

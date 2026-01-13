# 📝 Simple To-Do App (Flask + MySQL + JWT)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)
![MySQL](https://img.shields.io/badge/DB-MySQL-orange.svg)
![JWT](https://img.shields.io/badge/Auth-JWT-green.svg)

Este es un sistema de gestión de tareas desarrollado con un enfoque en el **Backend**, diseñado para ofrecer una experiencia de usuario segura y persistente. La aplicación permite a los usuarios gestionar sus tareas personales tras un proceso de autenticación robusto.

## 🚀 Características Principales

- **Autenticación Segura:** Sistema de registro e inicio de sesión con contraseñas encriptadas mediante `generate_password_hash`.
- **Seguridad con JWT:** Implementación de **JSON Web Tokens** para el manejo de sesiones mediante cookies, incluyendo protección y redirección automática si el token expira o no existe.
- **Base de Datos Relacional:** Uso de **MySQL** para la persistencia de datos y **SQLAlchemy** como ORM para realizar operaciones CRUD eficientes.
- **Funcionalidad Completa (CRUD):** Los usuarios pueden añadir tareas, marcarlas como completadas (con efecto visual de tachado) y eliminarlas de la base de datos.
- **Interfaz Responsiva:** Diseño adaptado a dispositivos móviles y escritorio mediante el uso de Media Queries en CSS.
- **Gestión de Errores:** Páginas personalizadas para manejar errores de rutas no encontradas (404) y fallos internos del servidor (500).

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3, Flask.
- **Base de Datos:** MySQL con el conector PyMySQL.
- **ORM:** Flask-SQLAlchemy.
- **Seguridad:** Flask-JWT-Extended y Werkzeug Security.
- **Frontend:** HTML5, CSS3 y el motor de plantillas Jinja2.

## 📋 Requisitos Previos

Necesitarás tener instalado:
- **Python 3.x**
- **MySQL Server** activo.

Instala las dependencias con el siguiente comando:
```bash
pip install flask flask_sqlalchemy flask_jwt_extended pymysql

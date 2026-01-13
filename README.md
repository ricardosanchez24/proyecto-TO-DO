# 📝 Simple To-Do App (Flask + MySQL + JWT)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)
![MySQL](https://img.shields.io/badge/DB-MySQL-orange.svg)
![JWT](https://img.shields.io/badge/Auth-JWT-green.svg)

Este es un gestor de tareas (To-Do List) robusto desarrollado con un enfoque en el **Backend**. La aplicación permite a los usuarios registrarse, iniciar sesión de forma segura y gestionar sus tareas personales con persistencia de datos profesional.

## 🚀 Características principales

- **Sistema de Autenticación:** Registro e inicio de sesión con encriptación de contraseñas mediante `werkzeug.security`.
- **Seguridad con JWT:** Gestión de sesiones mediante **JSON Web Tokens** almacenados en cookies seguras, con redirección automática si el token expira.
- **Persistencia de Datos:** Integración con **MySQL** utilizando el ORM **SQLAlchemy** para un manejo eficiente de la base de datos.
- **Operaciones CRUD:** Los usuarios pueden agregar, visualizar, marcar como completadas y eliminar sus propias tareas de forma independiente.
- **Arquitectura Limpia:** Uso de plantillas base (**Jinja2**) para evitar repetición de código y estilos CSS centralizados.
- **Manejo de Errores:** Páginas personalizadas para errores de servidor (500) y rutas no encontradas (404).

## 🛠️ Tecnologías utilizadas

- **Backend:** Python, Flask.
- **Base de Datos:** MySQL con PyMySQL.
- **ORM:** Flask-SQLAlchemy.
- **Seguridad:** Flask-JWT-Extended.
- **Frontend:** HTML5, CSS3 (Diseño responsivo).

## 📋 Requisitos previos

Asegúrate de tener instalado:
- Python 3.x
- MySQL Server

Instala las dependencias necesarias:
```bash
pip install flask flask_sqlalchemy flask_jwt_extended pymysql

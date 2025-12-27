# Importa los módulos necesarios de la biblioteca Flask
from flask import Flask, render_template, url_for, redirect, request, jsonify, make_response, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies
from sqlalchemy.exc import IntegrityError

# 1. Inicialización de la Aplicación
app = Flask(__name__) 

# 2. Almacén de Datos
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['SECRET_KEY'] = 'mi_clave_secreta'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://root:123456789@localhost/lista_tareas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)

class Usuario(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     nombre = db.Column(db.String(50), nullable = False, unique = True)
     contraseña = db.Column(db.String(260), nullable = False)
     
     def __repr__(self):
          return f'usuario: {self.nombre} '

class Tarea(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     contenido = db.Column(db.String(200), nullable = True)
     completada = db.Column(db.Boolean, default = False)
     id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = True)
     
     def __repr__(self):
          return f'tarea: {self.id} '

# 3. Definición de la Ruta Principal (Home)

@app.route('/', methods = ['POST','GET'])
@jwt_required()
def formulario_backend():
    usuario_actual = int(get_jwt_identity())
    if request.method == 'POST':
        nueva_tarea = request.form.get('tarea')
        if nueva_tarea:
            nueva_tarea_db = Tarea(contenido=nueva_tarea, id_usuario=usuario_actual) 
            try:
                db.session.add(nueva_tarea_db)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                return "Error al agregar la tarea. Inténtalo de nuevo."    
        
        return redirect(url_for('formulario_backend'))

    tareas_db = Tarea.query.filter_by(id_usuario=usuario_actual).all()
    return render_template('index.html', tareas=tareas_db)

@app.route('/eliminar/<int:id_tarea>', methods = ['POST'])

def eliminar_tarea(id_tarea):
        
        tarea_eliminar = Tarea.query.get_or_404(id_tarea)
        db.session.delete(tarea_eliminar)
        db.session.commit()

        return redirect(url_for('formulario_backend'))

@app.route('/completar/<int:tarea_id>', methods = ['POST'])
def completar_tarea(tarea_id):
      
    actualizar_tarea = Tarea.query.get_or_404(tarea_id)
    
    actualizar_tarea.completada = not actualizar_tarea.completada

    db.session.commit()
 
    return redirect(url_for('formulario_backend'))     

@app.route('/registro', methods = ['POST','GET'])
def registro_usuario():
    
    if request.method == 'POST':
        
        nombre = request.form.get('nombre')
        contraseña = request.form.get('contraseña')
        
        if nombre and contraseña:
            contraseña_encriptada = generate_password_hash(contraseña)
            nuevo_usuario_db = Usuario(nombre=nombre, contraseña=contraseña_encriptada) 
            try:
                db.session.add(nuevo_usuario_db)
                db.session.commit()
            except IntegrityError: #error de integridad de datos (por corrupcion,inconsistencia,duplicacion)
                db.session.rollback()
                return "El nombre de usuario ya existe. Por favor, elige otro."
            except Exception as e: #error general
                db.session.rollback()
                return f"Error al registrar el usuario: {str(e)}"
                
        flash('Registro exitoso. Por favor, inicia sesión.')
        return redirect(url_for('login_usuario'))

    return render_template('registro.html')  

@app.route('/login', methods = ['POST','GET'])
def login_usuario():
    
    if request.method == 'POST':
        
        nombre = request.form.get('nombre')
        contraseña = request.form.get('contraseña')
        
        usuario_db = Usuario.query.filter_by(nombre=nombre).first()
        
        if usuario_db and check_password_hash(usuario_db.contraseña, contraseña):
            token_acceso = create_access_token(identity=str(usuario_db.id))
            respuesta = redirect(url_for('formulario_backend'))
            set_access_cookies(respuesta, token_acceso)
            return respuesta 
        else:
            flash('Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.')
            return redirect(url_for('login_usuario'))

    return render_template('login.html')               

@app.route('/logout', methods=['POST'])
def logout_usuario():
    respuesta = redirect(url_for('login_usuario'))
    unset_jwt_cookies(respuesta)
    return respuesta

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno_del_servidor(e):
    return render_template('500.html'), 500

@jwt.expired_token_loader # Cuando el token ha expirado
def token_expirado(jwt_header, jwt_payload):
    # Redirigir al login si la sesión caducó
    return redirect(url_for('login_usuario'))

@jwt.unauthorized_loader # Cuando no hay token presente
def sin_token(razon):
    # Si intenta entrar sin cookie, mandarlo al login
    return redirect(url_for('login_usuario'))

if __name__ == '__main__':
    with app.app_context():
         #db.drop_all()
         db.create_all()

    app.run(debug=True)
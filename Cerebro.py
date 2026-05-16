from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # 1. Importamos CORS
from datetime import datetime

app = Flask(__name__)
CORS(app) # 2. Habilitamos CORS para que el navegador web no bloquee la conexión

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/fieldsense_db' # (Asegúrate de que esta línea tenga tu usuario/contraseña correcto que funcionó)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Lectura(db.Model):
    __tablename__ = 'lecturas'
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(50), nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    humedad = db.Column(db.Float, nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# --- Endpoint para RECIBIR datos (El que ya teníamos) ---
@app.route('/api/lecturas', methods=['POST'])
def recibir_lectura():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "No se recibió un JSON válido"}), 400
    try:
        nueva_lectura = Lectura(
            sensor_id=datos.get('sensor_id'),
            temperatura=datos.get('temperatura'),
            humedad=datos.get('humedad'),
            latitud=datos.get('latitud'),
            longitud=datos.get('longitud')
        )
        db.session.add(nueva_lectura)
        db.session.commit()
        return jsonify({"mensaje": "Datos registrados exitosamente", "id": nueva_lectura.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# --- NUEVO: Endpoint para ENTREGAR datos a la página web ---
@app.route('/')
def hola():
    return "<h1>Servidor FieldSense Activo 🌍</h1><p>El cerebro esta funcionando correctamente.</p>"
@app.route('/api/lecturas', methods=['GET'])
def obtener_lecturas():
    try:
        # Buscamos las últimas 10 lecturas en la base de datos, ordenadas de la más reciente a la más vieja
        lecturas = Lectura.query.order_by(Lectura.id.desc()).limit(10).all()
        
        # Armamos una lista de diccionarios para enviarla como JSON
        resultado = []
        for l in lecturas:
            resultado.append({
                "sensor_id": l.sensor_id,
                "temperatura": l.temperatura,
                "humedad": l.humedad,
                # Formateamos la hora para que se vea bonita en la gráfica (ej. 14:30:00)
                "hora": l.fecha_hora.strftime("%H:%M:%S") 
            })
            
        # Invertimos la lista para que la gráfica vaya de izquierda (viejo) a derecha (nuevo)
        return jsonify(resultado[::-1]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # '0.0.0.0' le dice a tu PC: "Acepta conexiones de cualquier lado (incluyendo Ngrok)"
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
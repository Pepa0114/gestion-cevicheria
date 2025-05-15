from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Saldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metodo_pago = db.Column(db.String(20), unique=True, nullable=False)
    saldo = db.Column(db.Float, nullable=False)
    monto_inicial = db.Column(db.Float, nullable=False)

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    metodo_pago = db.Column(db.String(20), nullable=False)

class Gasto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    metodo_pago = db.Column(db.String(20), nullable=False)  # <-- Nueva columna


class Transferencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    metodo_origen = db.Column(db.String(20), nullable=False)
    metodo_destino = db.Column(db.String(20), nullable=False)
    monto = db.Column(db.Float, nullable=False)

class ROA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10), nullable=False)      # 'diario', 'semanal', 'mensual'
    periodo = db.Column(db.String(20), nullable=False)   # '2025-05-15', '2025-W20', '2025-05'
    total_ventas = db.Column(db.Float, default=0.0)
    activo_total = db.Column(db.Float, default=0.0)
    roa = db.Column(db.Float, default=0.0)

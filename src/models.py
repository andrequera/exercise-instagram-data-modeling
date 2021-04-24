import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    empresa = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    telefono = Column(Integer)

class Cotizacion(Base):
    __tablename__ = 'cotizacion'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    producto = Column(String(250))
    descripcion = Column(String(250))
    paletas = Column(Integer, nullable=False)
    botellas = Column(Integer)
    sku= Column(String(250), nullable=False)
    total = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship(Cliente)

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)
    nombre_cliente = Column(String(50))
    fecha = Column(DateTime,default=datetime.datetime.utcnow)
    sku = Column(String(50))
    producto = Column(String(50))
    paleta = Column(Integer)
    cantidad = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship(Cliente)

class Inventario(Base):
    __tablename__='inventario'
    id = Column(Integer, primary_key=True)
    sku = Column(String(50))
    producto = Column(String(50))
    caja = Column(Integer)
    cantidad = Column(Integer)
    precio = Column(Integer)
    fecha = Column(DateTime,default=datetime.datetime.utcnow)

class Producto(Base):
    __tablename__='producto'
    id= Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String(50))
    paleta = Column(Integer)
    cantidad = Column(Integer)
    sku = Column(String(50), ForeignKey ('inventario.sku'))
    inventario = relationship(Inventario)

class Pedidos_Productos(Base):
    __tablename__='pedidos_productos'
    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'))
    pedido = relationship(Pedido)
    producto_id = Column(Integer, ForeignKey('producto.id'))
    producto = relationship(Producto)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
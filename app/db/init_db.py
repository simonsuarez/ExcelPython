from db.base import Base
from db.conexionBD import engine
# Asegura que los modelos se importen para crear las tablas
import models.user_model  # noqa: F401

Base.metadata.create_all(bind=engine)

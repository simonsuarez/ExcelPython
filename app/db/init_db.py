from db.base import Base
from db.conexionBD import engine
from models.user_model import Usuario

Base.metadata.create_all(bind=engine)

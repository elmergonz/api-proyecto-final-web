from models.baseModel import Base

from typing import Optional

class Patient(Base):
    cedula: str = '' # lo unico que estara en español xD

    # -- optionals: Estas son las caracteristicas que se deberian editar  --

    foto: str = ''
    email: str = ''
    bloodType: str = ''
    alergies: str = ''

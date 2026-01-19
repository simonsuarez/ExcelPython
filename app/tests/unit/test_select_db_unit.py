# tests/unit/test_comprobar_conexion_db.py
from services.user_service import comprobar_conexion_db
from unittest.mock import MagicMock
import pytest

@pytest.mark.unit
def test_comprobar_conexion_db_ok():
    db = MagicMock()
    db.execute.return_value.scalar.return_value = 1

    result = comprobar_conexion_db(db)

    assert result == {"databases": 1}

@pytest.mark.unit
def test_comprobar_conexion_db_error():
    db = MagicMock()
    db.execute.side_effect = Exception("DB down")

    result = comprobar_conexion_db(db)

    assert result["databases"] == "error"
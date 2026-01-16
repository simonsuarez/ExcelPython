\c excelDB

CREATE TABLE IF NOT EXISTS prueba (
    id SERIAL PRIMARY KEY,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descripcion TEXT NOT NULL
);

INSERT INTO prueba (descripcion) 
VALUES ('Este registro se generó al inicializar el servicio PostgreSQL a través de docker-compose');
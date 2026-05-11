"""create table entradas(
    cedula varchar(10) NOT NULL primary key,
    valor_inmueble numeric NOT NULL,
    tasa_capitalizacion numeric NOT NULL,
    edad integer NOT NULL,
    plazo_simulacion integer NOT NULL,
    porcentaje_LTV numeric NOT NULL
);"""
INSERT INTO entradas (cedula, valor_inmueble, tasa_capitalizacion, edad, plazo_simulacion, porcentaje_LTV) VALUES
('1234567890', 100000.00, 5.0, 65, 20, 80.0),
('0987654321', 150000.00, 4.5, 70, 15, 75.0),
('1122334455', 200000.00, 6.0, 60, 25, 85.0);

SELECT * FROM entradas
WHERE cedula = '1234567890';

UPDATE entradas
SET valor_inmueble = 120000,
    tasa_capitalizacion = 5.5,
    edad = 66,
    plazo_simulacion = 22,
    porcentaje_LTV = 82.0
WHERE cedula = '1234567890';


DELETE FROM entradas
WHERE cedula = '1234567890';
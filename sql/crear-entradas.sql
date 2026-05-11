create table entradas(
    cedula varchar(10) NOT NULL primary key,
    valor_inmueble NOT NULL,
    tasa_capitalizacion NOT NULL,
    edad NOT NULL,
    plazo_simulacion NOT NULL,
    porcentaje_LTV NOT NULL
);